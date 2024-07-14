# openai_assistant/thread_manager.py
from typing import Optional
from .utils import get_openai_client


async def list_messages(thread_id: str, limit: int = 20, order: str = 'desc', after: Optional[str] = None,
                        before: Optional[str] = None):
    try:
        return await get_openai_client().beta.threads.messages.list(thread_id=thread_id, limit=limit, order=order,
                                                                    after=after, before=before)
    except Exception as e:
        print(f"An error occurred while retrieving messages: {e}")
        return None


async def retrieve_message(thread_id: str, message_id: str):
    return await get_openai_client().beta.threads.messages.retrieve(thread_id=thread_id, message_id=message_id)


async def create_thread(messages: Optional[list] = None, metadata: Optional[dict] = None):
    return await get_openai_client().beta.threads.create(messages=messages, metadata=metadata)


async def retrieve_thread(thread_id: str):
    return await get_openai_client().beta.threads.retrieve(thread_id)


async def modify_thread(thread_id: str, metadata: dict):
    return await get_openai_client().beta.threads.modify(thread_id, metadata=metadata)


async def delete_thread(thread_id: str):
    return await get_openai_client().beta.threads.delete(thread_id)


async def send_message(thread_id: str, content: str, role: str = "user"):
    return await get_openai_client().beta.threads.messages.create(thread_id=thread_id, role=role, content=content)


async def send_image_with_id(thread_id: str, image_id: str, role: str = "user"):
    return await get_openai_client().beta.threads.messages.create(thread_id=thread_id, role=role,
                                                                  content=[{"type": "image_file", "image_file": {"file_id": image_id}}])


async def send_image_with_url(thread_id: str, image_url: str, role: str = "user"):
    return await get_openai_client().beta.threads.messages.create(thread_id=thread_id, role=role,
                                                                  content=[{"type": "image_url", "image_url": {"url": image_url}}])


async def create_run(thread_id: str, assistant_id: str):
    return await get_openai_client().beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)


async def get_runs_by_thread(thread_id: str):
    return await get_openai_client().beta.threads.runs.list(thread_id=thread_id)


async def submit_tool_outputs_and_poll(thread_id: str, run_id: str, tool_outputs: list):
    return await get_openai_client().beta.threads.runs.submit_tool_outputs_and_poll(
        thread_id=thread_id,
        run_id=run_id,
        tool_outputs=tool_outputs
    )
