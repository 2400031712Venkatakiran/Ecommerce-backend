from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# ==========================
# User
# ==========================

class RegisterUser(BaseModel):
    full_name: str
    email: str
    password: str
    phone: str


class LoginUser(BaseModel):
    email: str
    password: str


class UpdateProfile(BaseModel):
    full_name: str
    phone: str


class ChangePassword(BaseModel):
    old_password: str
    new_password: str


# ==========================
# Category
# ==========================

class CreateCategory(BaseModel):
    category_name: str
    description: str


class UpdateCategory(BaseModel):
    category_name: Optional[str] = None
    description: Optional[str] = None


# ==========================
# Product
# ==========================

class CreateProduct(BaseModel):
    product_name: str
    description: str
    price: float
    stock: int
    brand: str
    category_id: int


class UpdateProduct(BaseModel):
    product_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    brand: Optional[str] = None
    category_id: Optional[int] = None


class UpdateStock(BaseModel):
    stock: int


# ==========================
# Cart
# ==========================

class AddCartItem(BaseModel):
    product_id: int
    quantity: int


class UpdateCartItem(BaseModel):
    quantity: int


class RemoveCartItem(BaseModel):
    product_id: int


# ==========================
# Wishlist
# ==========================

class WishlistItem(BaseModel):
    product_id: int


# ==========================
# Shipping Address
# ==========================

class ShippingAddress(BaseModel):
    full_name: str
    phone: str
    address: str
    city: str
    state: str
    country: str
    postal_code: str


# ==========================
# Coupon
# ==========================

class CreateCoupon(BaseModel):
    coupon_code: str
    discount_percentage: float
    expiry_date: datetime
    minimum_purchase: float


class ApplyCoupon(BaseModel):
    coupon_code: str


# ==========================
# Order
# ==========================

class CreateOrder(BaseModel):
    shipping_address: str
    payment_method: str
    coupon_code: Optional[str] = None


class UpdateOrderStatus(BaseModel):
    order_status: str


# ==========================
# Payment
# ==========================

class PaymentRequest(BaseModel):
    payment_method: str
    amount: float


# ==========================
# Review
# ==========================

class CreateReview(BaseModel):
    product_id: int
    rating: int
    review_text: str


class UpdateReview(BaseModel):
    rating: Optional[int] = None
    review_text: Optional[str] = None