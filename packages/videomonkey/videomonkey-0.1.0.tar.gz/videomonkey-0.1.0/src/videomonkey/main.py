import whisper
import os
import subprocess
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
import byzerllm
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import time
import ffmpeg
from typing import List,Optional

console = Console()


@byzerllm.prompt()
def generate_video_processing_code(
    description: str, input_video_path: str, output_video_path: str, current_pos: float
) -> str:
    """
    根据用户描述生成使用 ffmpeg-python 和 moviepy 处理视频的 Python 代码。

    输入描述:
    {{ description }}

    请生成相应的 Python 代码，包括必要的导入语句。
    确保代码是完整且可执行的。
    使用 ffmpeg-python 和 moviepy 库来实现视频处理功能。

    待处理视频路径：{{ input_video_path }}
    输出视频路径：{{ output_video_path }}
    当前视频位置（秒）：{{ current_pos }}

    1. 生成的代码在juypyter notebook中运行,但不要调用display()或show()函数。
    2. 不要有main函数 或者 if __name__ == "__main__": 代码块
    3. 如果定义了函数，请确保函数被调用
    4. 生成的代码不要带 ```python ``` 代码块标识
    5. 请考虑使用 current_pos 参数作为视频处理的起始点
    6. 如果你最后采用了moviepy，拼接视频请使用CompositeVideoClip。

    生成的代码请用 <CODE></CODE> 标签括起来。
    """


def extract_code(response: str) -> str:
    import re

    pattern = re.compile(r"<CODE>(.*?)</CODE>", re.DOTALL)
    match = pattern.search(response)
    if match:
        return match.group(1).strip()
    return ""


from rich.panel import Panel
from rich.syntax import Syntax


import os

def execute_video_processing(
    description: str, input_video: str, output_video: str, dry_run: bool = False, current_pos: float = 0.0
):    
    output_dir = os.path.dirname(output_video)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        console.print(f"[bold green]Created output directory: {output_dir}[/bold green]")

    llm = byzerllm.ByzerLLM.from_default_model("deepseek_chat")
    code = (
        generate_video_processing_code.with_llm(llm)
        .with_extractor(extract_code)
        .run(
            description=description,
            input_video_path=input_video,
            output_video_path=output_video,
            current_pos=current_pos,
        )
    )

    # Create a syntax-highlighted version of the code
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)

    # Create a panel with the syntax-highlighted code
    console.print()
    console.print()
    panel = Panel(
        syntax,
        title="[bold green]Generated Code[/bold green]",
        border_style="green",
        expand=False,
    )

    # Print the panel
    console.print(panel)

    console.print()
    console.print()

    if dry_run:
        console.print(
            "[bold yellow]Dry run mode enabled. Code execution skipped.[/bold yellow]"
        )
        return

    console.print("[bold yellow]Executing generated code...[/bold yellow]")

    # Create a local scope with necessary imports and variables
    local_scope = {
        "ffmpeg": ffmpeg,
        "VideoFileClip": VideoFileClip,
        "concatenate_videoclips": concatenate_videoclips,
        "vfx": vfx,
        "console": console,
        "input_video": input_video,
        "output_video": output_video,
    }

    if code.startswith("```python"):
        # Remove the first and last line if it contains the code block identifier
        code = "\n".join(code.split("\n")[1:-1])

    # Generate and save the .py file
    if not dry_run:
        py_file_path = os.path.splitext(output_video)[0] + '.py'
        with open(py_file_path, 'w') as py_file:
            py_file.write(code)
        console.print(f"[bold green]Generated Python code saved to: {py_file_path}[/bold green]")    

    try:
        exec(code, local_scope)
        console.print(
            "[bold green]Video processing completed successfully![/bold green]"
        )
    except Exception as e:
        console.print(f"[bold red]Error during video processing: {str(e)}[/bold red]")


def generate_subtitle(video_path: str, output_path: str):
    with console.status("[bold green]Loading Whisper model...") as status:
        start_time = time.time()
        model = whisper.load_model("large")
        end_time = time.time()
        console.print(
            f"[bold green]✓[/bold green] Whisper model loaded in {end_time - start_time:.2f} seconds"
        )

    with Progress(
        SpinnerColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Transcribing video...", total=None)
        start_time = time.time()
        result = model.transcribe(video_path)
        end_time = time.time()
        progress.update(task, completed=100)
        console.print(
            f"[bold green]✓[/bold green] Video transcribed in {end_time - start_time:.2f} seconds"
        )

    with console.status("[bold green]Processing and writing subtitle file...") as status:
        segments = result["segments"]
        processed_segments = []

        for i, segment in enumerate(segments):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]
            
            # Add the current segment
            processed_segments.append((start, end, text))
            
            # If there's a next segment, check for gap
            if i < len(segments) - 1:
                next_start = segments[i + 1]["start"]
                if end < next_start:
                    # Add an empty segment to fill the gap
                    processed_segments.append((end, next_start, ""))

        with open(output_path, "w", encoding="utf-8") as f:
            for start, end, text in processed_segments:
                f.write(f"{start:.2f} {end:.2f} {text}\n")

    console.print("[bold green]✓[/bold green] Subtitle generated and processed successfully")


@byzerllm.prompt()
def edit_subtitle(subtitle_text: str) -> str:
    """
    从给定的字幕文本中删除不包含对话的部分。
    只保留包含实际口语内容的行。

    输入字幕格式:
    开始时间 结束时间 文本内容

    以下是字幕文本:

    {{ subtitle_text }}

    请以相同格式输出编辑后的字幕,并将编辑后的字幕文本用<RESPONSE></RESPONSE>标签括起来。
    """


def extract_regex_pattern(regex_block: str) -> str:
    import re

    pattern = re.search(r"<RESPONSE>(.*)</RESPONSE>", regex_block, re.DOTALL)
    if pattern is None:
        console.print(
            f"[bold red] No regex pattern found in the generated block \n {regex_block}[/bold red]"
        )
        raise None
    return pattern.group(1)


def process_video(video_path: str, output_path: str, edited_srt_path: Optional[str] = None):
    with Progress() as progress:
        if edited_srt_path is None:
            task1 = progress.add_task("[green]Generating subtitle...", total=100)
            subtitle_path = os.path.splitext(video_path)[0] + ".srt"
            generate_subtitle(video_path, subtitle_path)
            progress.update(task1, completed=100)

            task2 = progress.add_task("[yellow]Editing subtitle...", total=100)
            with open(subtitle_path, "r", encoding="utf-8") as f:
                subtitle_text = f.read()

            llm = byzerllm.ByzerLLM.from_default_model("deepseek_chat")
            edited_subtitle = (
                edit_subtitle.with_llm(llm)
                .with_extractor(extract_regex_pattern)
                .run(subtitle_text=subtitle_text)
            )

            edited_subtitle_path = os.path.splitext(subtitle_path)[0] + "_edited.srt"
            with open(edited_subtitle_path, "w", encoding="utf-8") as f:
                f.write(edited_subtitle)
            progress.update(task2, completed=100)
        else:
            edited_subtitle_path = edited_srt_path
            console.print(
                "[bold green]✓[/bold green] Using provided edited subtitle file"
            )

        task3 = progress.add_task("[blue]Processing video...", total=100)
        process_video_with_subtitle(video_path, edited_subtitle_path, output_path)
        progress.update(task3, completed=100)

    console.print("[bold green]✓[/bold green] Video processed successfully")


def process_video_with_subtitle(video_path: str, subtitle_path: str, output_path: str):
    # Read the subtitle file
    with open(subtitle_path, "r") as f:
        subtitle_lines = f.readlines()

    # Parse the subtitle timestamps
    timestamps = []
    for line in subtitle_lines:
        parts = line.strip().split()
        if len(parts) >= 2:
            start, end = float(parts[0]), float(parts[1])
            timestamps.append((start, end))

    # Sort timestamps and merge overlapping segments
    timestamps.sort(key=lambda x: x[0])
    merged_timestamps = []
    for start, end in timestamps:
        if not merged_timestamps or start > merged_timestamps[-1][1]:
            merged_timestamps.append((start, end))
        else:
            merged_timestamps[-1] = (
                merged_timestamps[-1][0],
                max(merged_timestamps[-1][1], end),
            )

    # Load the video
    video = VideoFileClip(video_path)

    # Cut the video based on the merged timestamps
    clips = []
    for start, end in merged_timestamps:
        clip = video.subclip(start, end)
        clips.append(clip)

    # Add transitions between clips
    final_clips = []
    for i, clip in enumerate(clips):
        if i > 0:
            # Add a fade transition
            clip = clip.fx(vfx.fadeout, duration=0.5).fx(vfx.fadein, duration=0.5)
        final_clips.append(clip)

    # Concatenate all clips
    final_video = concatenate_videoclips(final_clips)

    # Write the result to a file
    final_video.write_videofile(output_path)

    # Close the video to free up system resources
    video.close()
