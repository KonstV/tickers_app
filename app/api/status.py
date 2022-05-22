from fastapi import APIRouter

router = APIRouter(
    prefix=''
)

@router.get('/status')
def status():
    return "Online"
