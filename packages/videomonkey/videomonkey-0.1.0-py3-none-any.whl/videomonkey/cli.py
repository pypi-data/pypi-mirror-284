import argparse
import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import byzerllm
from videomonkey.main import generate_subtitle, edit_subtitle, process_video, execute_video_processing

console = Console()

def initialize_video_monkey():
    console.print(Panel.fit(
        Text("🚀 Initializing Video Monkey", style="bold cyan"),
        border_style="cyan"
    ))

    def print_status(message, status):
        if status == "success":
            console.print(f"[bold green]✓[/bold green] {message}")
        elif status == "warning":
            console.print(f"[bold yellow]![/bold yellow] {message}")
        elif status == "error":
            console.print(f"[bold red]✗[/bold red] {message}")
        else:
            console.print(f"  {message}")

    with console.status("[bold blue]Checking system requirements...[/bold blue]") as status:
        # Check if Ray is running
        status.update("[bold blue]Checking Ray status...[/bold blue]")
        ray_status = subprocess.run(["ray", "status"], capture_output=True, text=True)
        if ray_status.returncode != 0:
            print_status("Ray is not running. Starting Ray...", "warning")
            try:
                subprocess.run(["ray", "start", "--head"], check=True)
                print_status("Ray started successfully.", "success")
            except subprocess.CalledProcessError:
                print_status("Failed to start Ray. Please start it manually.", "error")
                return False

        # Check if deepseek_chat model is available
        status.update("[bold blue]Checking deepseek_chat model availability...[/bold blue]")
        try:
            result = subprocess.run(
                ["easy-byzerllm", "chat", "deepseek_chat", "你好"],
                capture_output=True,
                text=True,
                timeout=30,
            )
            if result.returncode == 0:
                print_status("deepseek_chat model is available.", "success")
                return True
        except subprocess.TimeoutExpired:
            print_status("Command timed out. deepseek_chat model might not be available.", "error")
        except subprocess.CalledProcessError:
            print_status("Error occurred while checking deepseek_chat model.", "error")

        print_status("deepseek_chat model is not available. Please set it up manually.", "warning")
        return False

def main():
    parser = argparse.ArgumentParser(description="Video Monkey: Process videos By Chat")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Generate subtitle command
    generate_parser = subparsers.add_parser("generate_srt", help="Generate subtitle for a video")
    generate_parser.add_argument("video", help="Path to the video file")
    generate_parser.add_argument("-o", "--output", help="Output path for the subtitle file", default=None)

    # Edit subtitle command
    edit_parser = subparsers.add_parser("auto_edit_srt", help="Edit an existing subtitle file")
    edit_parser.add_argument("subtitle", help="Path to the subtitle file")
    edit_parser.add_argument("-o", "--output", help="Output path for the edited subtitle file", default=None)

    # Process video command
    process_parser = subparsers.add_parser("edit_video", help="Process a video to remove silent parts")
    process_parser.add_argument("video", help="Path to the video file")
    process_parser.add_argument("-o", "--output", help="Output path for the processed video", default=None)
    process_parser.add_argument("-s", "--srt", help="Path to the edited SRT file (optional)", default=None)

    # Add new command for custom video processing
    custom_process_parser = subparsers.add_parser("custom", help="Process video using custom description")
    custom_process_parser.add_argument("video", help="Path to the input video file")
    custom_process_parser.add_argument("description", help="Description of the video processing task")
    custom_process_parser.add_argument("-o", "--output", help="Output path for the processed video", default=None)
    custom_process_parser.add_argument("--dry_run", help="without execute", action="store_true")
    custom_process_parser.add_argument("--current_pos", type=float, help="Current position in the video (in seconds)", default=0.0)

    args = parser.parse_args()

    if not initialize_video_monkey():
        console.print("[red]Initialization failed. Please resolve the issues and try again.[/red]")
        return

    if args.command == "generate_srt":
        video_path = args.video
        if args.output:
            subtitle_path = args.output
        else:
            subtitle_path = os.path.splitext(video_path)[0] + ".srt"
        generate_subtitle(video_path, subtitle_path)
        console.print(f"[green]Subtitle generated: {subtitle_path}[/green]")

    elif args.command == "auto_edit_srt":
        subtitle_path = args.subtitle
        if args.output:
            edited_subtitle_path = args.output
        else:
            base_name = os.path.basename(subtitle_path)
            name, ext = os.path.splitext(base_name)
            edited_subtitle_path = f"{name}_edited{ext}"
        
        with open(subtitle_path, "r", encoding="utf-8") as f:
            subtitle_text = f.read()
        
        llm = byzerllm.ByzerLLM.from_default_model("deepseek_chat")
        edited_subtitle = edit_subtitle(subtitle_text)
        
        with open(edited_subtitle_path, "w", encoding="utf-8") as f:
            f.write(edited_subtitle)
        console.print(f"[green]Edited subtitle saved: {edited_subtitle_path}[/green]")

    elif args.command == "edit_video":
        video_path = args.video
        if args.output:
            output_path = args.output
        else:
            base_name = os.path.basename(video_path)
            name, ext = os.path.splitext(base_name)
            output_path = f"{name}_processed{ext}"

        process_video(video_path, output_path, args.srt)
        console.print(f"[green]Processed video saved: {output_path}[/green]")
    elif args.command == "custom":
        video_path = args.video
        description = args.description
        if args.output:
            output_path = args.output
        else:
            base_name = os.path.basename(video_path)
            name, ext = os.path.splitext(base_name)
            output_path = f"{name}_custom_processed{ext}"

        execute_video_processing(description, video_path, output_path, dry_run=args.dry_run, current_pos=args.current_pos)
        console.print(f"[green]Custom processed video saved: {output_path}[/green]")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()