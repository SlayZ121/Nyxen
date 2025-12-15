from typing import List, Optional, dict
from datetime import datetime
from pydantic import BaseModel


class StoryOptionsSchema(BaseModel):
	text:str
	node_id: Optional[int]=None

class StoryNodeBase(BaseModel):
	content:str
	is_ending:bool=False
	is_winning_ending:bool=False

class CompleteStoryNodeResponse(StoryNodeBase):
	id:int
	options:List[StoryOptionsSchema]=[]

	class Config:
		from_attributes = True




