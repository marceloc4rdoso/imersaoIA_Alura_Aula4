
def generation():
    generation_config = {
        "candidate_count": 1,
        "temperature": 0.5,
    }
    return generation_config

def safety():
    safety_settings = {
        "HARASSMENT": "BLOCK_NONE",
        "HATE": "BLOCK_NONE",
        "SEXUAL": "BLOCK_MEDIUM_AND_ABOVE",
        "DANGEROUS": "BLOCK_NONE",
    }
    return safety_settings
