from plus_sync.config import Config


def get_hashed_default() -> bool:
    config = Config.from_cmdargs()
    return config.hash_subject_ids
