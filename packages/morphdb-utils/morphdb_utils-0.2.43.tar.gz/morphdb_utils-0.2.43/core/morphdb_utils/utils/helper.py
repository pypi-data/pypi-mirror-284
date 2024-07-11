MORPH_STORAGE_PREFIX = "morph-storage://"


def get_presigned_url_path(file_path: str, team_slug: str, database_id: str) -> str:
    if file_path.startswith("morph-storage://"):
        return file_path
    return "{}vm/{}/{}/{}".format(
        MORPH_STORAGE_PREFIX,
        team_slug,
        database_id,
        file_path if not file_path.startswith("/") else file_path[1:],
    )
