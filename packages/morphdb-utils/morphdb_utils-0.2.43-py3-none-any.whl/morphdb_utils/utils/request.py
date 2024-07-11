def canonicalize_base_url(base_url: str) -> str:
    if base_url.startswith("http"):
        return base_url
    else:
        return f"https://{base_url}"
