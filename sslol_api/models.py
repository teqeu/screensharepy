from pydantic import BaseModel, Field, validator
from typing import List, Optional

class GuildJoinLeave(BaseModel):
    id: int
    memberId: str
    memberUsername: str
    guildid: str
    guildname: str
    joined_at: str
    left_at: Optional[str]

class Summary(BaseModel):
    total_tickets: int
    total_tickets_v2: int
    total_guild_records: int
    is_flagged: bool

class UserInfo(BaseModel):
    discord_id: str

class SearchResponse(BaseModel):
    found: bool
    ok: bool
    user: UserInfo
    tickets: List[dict]
    tickets_v2: List[dict]
    guild_join_leave: List[GuildJoinLeave]
    flagged: Optional[bool] = Field(default=None)
    summary: Summary

    @validator("flagged", pre=True, always=True)
    def parse_flagged(cls, v):
        if v is None:
            return None
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            return v.lower() == "true"
        if isinstance(v, int):
            return bool(v)
        return None
