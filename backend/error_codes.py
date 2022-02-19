from fastapi import HTTPException

# URL
NO_URL_FOUND = HTTPException(status_code=404, detail="No url found for alias")
INVALID_URL_PROVIDED = HTTPException(status_code=400, detail="Invalid URL provided")

# ALIAS
NO_ALIAS_PROVIDED = HTTPException(status_code=400, detail="Missing alias")
INVALID_ALIAS_LENGTH_PROVIDED = HTTPException(status_code=400, detail="Alias longer than url")
INVALID_ALIAS_PROVIDED = HTTPException(status_code=400,
                                       detail="Invalid alias, only alphanumeric symbols, dash or underscore are allowed"
                                       )

# 400
ALIAS_ALREADY_TAKEN = HTTPException(status_code=409, detail="Alias already taken")

# 500
INTERNAL_ERROR = HTTPException(status_code=500, detail="Internal server error")
