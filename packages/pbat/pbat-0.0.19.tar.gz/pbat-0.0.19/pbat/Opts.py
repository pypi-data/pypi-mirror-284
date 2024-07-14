from dataclasses import dataclass, field

ON_PUSH = 1

WINDOWS_2019 = "windows-2019"
WINDOWS_2022 = "windows-2022"
WINDOWS_LATEST = "windows-latest"

@dataclass
class Opts:
    debug: bool = False
    clean: bool = False
    curl_in_path: bool = False
    curl_user_agent: str = None
    curl_proxy: str = None
    download_test: bool = True
    unzip_test: bool = True
    zip_test: bool = True
    github: bool = False
    zip_in_path = False
    git_in_path = False
    tar_in_path = False
    patch_in_path = False
    github_workflow = False
    github_image: str = WINDOWS_LATEST
    github_on: int = ON_PUSH
    msys2_msystem: str = None
    use_sed: bool = False
    use_diff: bool = True
    env_path: list[str] = field(default_factory=list)
    clear_path: bool = False
    #main_def: str = None
    #order: list[str] = field(default_factory=list)
    #top: list[str] = field(default_factory=list)