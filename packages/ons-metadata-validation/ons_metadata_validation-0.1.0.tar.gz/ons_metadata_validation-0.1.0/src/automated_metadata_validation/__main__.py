import argparse
from typing import Optional

from automated_metadata_validation.outputs.excel_outputs import (
    outputs_main,
)
from automated_metadata_validation.processing.processing import (
    MetadataProcessor,
)


def main(
    md_filepath: str,
    role_config_key: str = "cmar",
    save_report: bool = True,
    create_corrected_version: bool = False,
    make_commented_copy: bool = True,
    save_dir: Optional[str] = None,
):
    # setup_logger(__file__, 2)

    processor = MetadataProcessor(
        md_filepath,
        role_config_key=role_config_key,
        save_report=save_report,
        create_corrected_version=create_corrected_version,
    )
    processor.main_process()
    return outputs_main(
        processor=processor,
        save_folder=save_dir,
        make_commented_copy=make_commented_copy,
    )


def main_cli() -> None:
    parser = argparse.ArgumentParser(description="validate metadata template")
    parser.add_argument(
        "md_filepath", type=str, help="the filepath to the metdata template"
    )
    parser.add_argument(
        "role_config_key",
        default="cmar",
        const="cmar",
        nargs="?",
        choices=["cmar", "full"],
        type=str,
        help="the role config to apply",
    )
    parser.add_argument(
        "-s",
        dest="save_report",
        default=True,
        type=bool,
        help="save the validation report",
    )
    parser.add_argument(
        "-c",
        dest="create_corrected_version",
        default=False,
        type=bool,
        help="create a corrected version of the template",
    )
    parser.add_argument(
        "-m",
        dest="make_commented_copy",
        default=True,
        type=bool,
        help="create a commented version of the template",
    )
    parser.add_argument(
        "-d",
        dest="save_dir",
        default=None,
        type=str,
        help="save report in directory, defaults to same location as metadata file",
    )

    args = parser.parse_args()

    main(
        args.md_filepath,
        args.role_config_key,
        args.save_report,
        args.create_corrected_version,
        args.make_commented_copy,
        args.save_dir,
    )


if __name__ == "__main__":
    main_cli()
