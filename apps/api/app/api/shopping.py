from fastapi import APIRouter

router = APIRouter()


@router.get("/shopping-list")
def get_shopping_list():
    return [
        {
            "ingredient": "Bread Flour",
            "needed": 5000,
            "unit": "g",
            "status": "buy",
        },
        {
            "ingredient": "Salt",
            "needed": 500,
            "unit": "g",
            "status": "stocked",
        },
        {
            "ingredient": "Starter Feed",
            "needed": 2000,
            "unit": "g",
            "status": "low",
        },
    ]
