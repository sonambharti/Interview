import uuid
from abc import ABC, abstractmethod
from typing import List, Dict, Set

# ==========================================
# 1. ENTITIES / MODELS
# ==========================================

class User:
    def __init__(self, name: str, phone: str, pincode: str):
        self.id: str = str(uuid.uuid4())
        self.name: str = name
        self.phone: str = phone
        self.pincode: str = pincode


class Dish:
    def __init__(self, name: str, price: float):
        self.id: str = str(uuid.uuid4())
        self.name: str = name
        self.price: float = price
        
        # Absolute granular accumulators for this specific item
        self.total_score_accumulated: float = 0.0
        self.total_rating_count: int = 0

    @property
    def average_rating(self) -> float:
        if self.total_rating_count == 0:
            return 0.0
        return round(self.total_score_accumulated / self.total_rating_count, 2)

    def register_new_score(self, score: float) -> None:
        """Enforces defensive validation guarantees before mutating data states"""
        if not (1.0 <= score <= 5.0):
            raise ValueError(f"Constraint Violation: Score {score} falls outside valid 1-5 boundaries.")
        self.total_score_accumulated += score
        self.total_rating_count += 1


class Restaurant:
    def __init__(self, name: str, pincodes: List[str], dishes: List[Dish]):
        self.id: str = str(uuid.uuid4())
        self.name: str = name
        self.serviceable_pincodes: Set[str] = set(pincodes)
        
        # O(1) Key-Value lookup map for menu items
        self.menu: Dict[str, Dish] = {dish.id: dish for dish in dishes}

    @property
    def average_rating(self) -> float:
        """
        Calculates the weighted Micro-Average across all dishes served.
        Formula: Sum(All Dish Scores) / Total(All Dish Rating Counts)
        """
        combined_score = sum(dish.total_score_accumulated for dish in self.menu.values())
        combined_count = sum(dish.total_rating_count for dish in self.menu.values())
        
        if combined_count == 0:
            return 0.0
            
        return round(combined_score / combined_count, 2)

    @property
    def primary_dish_price(self) -> float:
        """Determines baseline catalog entry price safely"""
        if not self.menu:
            return float('inf')
        return min(dish.price for dish in self.menu.values())

    def verify_dish_exists(self, dish_id: str) -> bool:
        return dish_id in self.menu

    def add_dish_rating(self, dish_id: str, score: float) -> None:
        self.menu[dish_id].register_new_score(score)


# ==========================================
# 2. FACTORY LAYER
# ==========================================

class UserFactory:
    @staticmethod
    def create_user(name: str, phone: str, pincode: str) -> User:
        return User(name, phone, pincode)


class RestaurantFactory:
    @staticmethod
    def create_restaurant(name: str, pincodes: List[str], dishes: List[Dish]) -> Restaurant:
        return Restaurant(name, pincodes, dishes)


# ==========================================
# 3. SINGLETON REPOSITORY / STORAGE
# ==========================================

class StorageContext:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageContext, cls).__new__(cls)
            cls._instance._init_storage()
        return cls._instance

    def _init_storage(self):
        self.users: Dict[str, User] = {}
        self.restaurants: Dict[str, Restaurant] = {}
        self.pincode_to_restaurants_map: Dict[str, Set[str]] = {}


# ==========================================
# 4. STRATEGY PATTERN FOR DISPLAY/SORTING
# ==========================================

class DisplayStrategy(ABC):
    @abstractmethod
    def sort(self, restaurants: List[Restaurant]) -> List[Restaurant]:
        pass


class PriceAscendingStrategy(DisplayStrategy):
    def sort(self, restaurants: List[Restaurant]) -> List[Restaurant]:
        return sorted(restaurants, key=lambda r: (r.primary_dish_price, r.name))


class RatingDescendingStrategy(DisplayStrategy):
    def sort(self, restaurants: List[Restaurant]) -> List[Restaurant]:
        return sorted(restaurants, key=lambda r: (-r.average_rating, r.name))


# ==========================================
# 5. CORE BUSINESS LOGIC SERVICE LAYER
# ==========================================

class FoodRatingSystem:
    def __init__(self):
        self._db = StorageContext()

    def register_user(self, name: str, phone: str, pincode: str) -> User:
        user = UserFactory.create_user(name, phone, pincode)
        self._db.users[user.id] = user
        return user

    def register_restaurant(self, name: str, pincodes: List[str], dishes: List[Dish]) -> Restaurant:
        restaurant = RestaurantFactory.create_restaurant(name, pincodes, dishes)
        self._db.restaurants[restaurant.id] = restaurant
        
        for pin in pincodes:
            if pin not in self._db.pincode_to_restaurants_map:
                self._db.pincode_to_restaurants_map[pin] = set()
            self._db.pincode_to_restaurants_map[pin].add(restaurant.id)
            
        return restaurant

    def rate_restaurant_dish(self, user_id: str, restaurant_id: str, dish_id: str, score: float) -> None:
        """Evaluates a menu item and updates overall corporate aggregates securely"""
        # Rule 1: Strict Range Guarding Check
        if not (1.0 <= score <= 5.0):
            raise ValueError(f"Operation Aborted: Rating score '{score}' must reside between 1.0 and 5.0.")
            
        # Rule 2: Verify System Context Integrity
        if user_id not in self._db.users:
            raise ValueError("Access Denied: Invalid User Session Identification.")
        if restaurant_id not in self._db.restaurants:
            raise ValueError("Targeting Error: Restaurant entity reference missing.")
        
        restaurant = self._db.restaurants[restaurant_id]
        if not restaurant.verify_dish_exists(dish_id):
            raise ValueError("Menu Mismatch: Targeted item is not sold by this restaurant.")

        # Atomic Execution down to the entity layer
        restaurant.add_dish_rating(dish_id, score)

    def show_serviceable_restaurants_for_user(self, user_id: str, strategy: DisplayStrategy) -> List[Restaurant]:
        user = self._db.users.get(user_id)
        if not user:
            raise ValueError("User Authentication failed.")
            
        user_pincode = user.pincode
        matching_ids = self._db.pincode_to_restaurants_map.get(user_pincode, set())
        serviceable_list = [self._db.restaurants[rid] for rid in matching_ids]
        
        return strategy.sort(serviceable_list)


# ==========================================
# 6. EXECUTABLE DRIVER VERIFICATION ENGINE
# ==========================================
if __name__ == "__main__":
    print("--- Booting Validated Rating Pipeline Engine ---")
    system = FoodRatingSystem()

    # Onboard users
    sheena = system.register_user("Sheena", "+918989898989", "500081")
    aditya = system.register_user("Aditya Sharma", "+919999999999", "500032")
    
    # Initialize multi-dish menu profiles
    chicken_biryani = Dish("Chicken Biryani", 350.0)
    classic_burger = Dish("Classic Veg Burger", 180.0)
    masala_dosa = Dish("Masala Dosa", 120.0)

    # Register Restaurants with complex menus
    r1 = system.register_restaurant("Grand Biryani Kitchen", ["500081"], [chicken_biryani, classic_burger])
    print(f"Registered {r1.name} with {len(r1.menu)} distinct items on the menu.")

    # Execute Dish-level Ratings
    print("\nExecuting user evaluations across discrete dishes...")
    system.rate_restaurant_dish(sheena.id, r1.id, chicken_biryani.id, 5.0)
    system.rate_restaurant_dish(aditya.id, r1.id, chicken_biryani.id, 4.0) # Biryani Avg = 4.5 (2 votes)
    
    system.rate_restaurant_dish(sheena.id, r1.id, classic_burger.id, 2.0)  # Burger Avg = 2.0 (1 vote)
    
    # Let's test the validation logic with an error catch
    try:
        print("\nAttempting to ingest illegal out-of-bounds score (6.5)...")
        system.rate_restaurant_dish(sheena.id, r1.id, chicken_biryani.id, 6.5)
    except ValueError as err:
        print(f">>> Successfully caught and blocked bad input rule: {err}")

    # Display dynamically recalculated weighted results
    print(f"\n--- Menu Metrics for {r1.name} ---")
    print(f"-> Chicken Biryani Avg Rating: {chicken_biryani.average_rating}")
    print(f"-> Classic Veg Burger Avg Rating: {classic_burger.average_rating}")
    print(f"=== Weighted Combined Restaurant Avg Rating: {r1.average_rating} ===")
    print("   (Calculation: (5.0 + 4.0 + 2.0) / 3 total reviews = 3.67)")