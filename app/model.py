from sqlalchemy import Column, Integer, String, DATETIME, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base
class User(Base):
    __tablename__="User"
    user_id=Column(Integer,primary_key=True)
    full_name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    phone_number=Column(String,nullable=False)
    role=Column(String,nullable=False)
    is_active=Column(String,nullable=False)
    reviews=relationship("Review",back_populates="user")
    orders=relationship("Order",back_populates="user")
    wishlist=relationship("Wishlist",back_populates="user")
    cart=relationship("Cart",back_populates="user")
class Category(Base):
    __tablename__="Category"
    category_id=Column(Integer,primary_key=True)
    category_name=Column(String,nullable=False)
    description=Column(String)
    product=relationship("Product",back_populates="category")

class Product(Base):
    __tablename__="Product"
    product_id=Column(Integer,primary_key=True)
    product_nam=Column(String)
    description=Column(String)
    price=Column(Float)
    stock=Column(Integer)
    brand=Column(String)
    image=Column(String)
    category_id=Column(Integer,ForeignKey("Category.category_id"))
    category=relationship("Category",back_populates="product")
    reviews=relationship("Review",back_populates="product")
    orderitem=relationship("OrderItem",back_populates="product")
    cartitem=relationship("Cartitem",back_populates="product")

class Cart(Base):
    __tablename__="Cart"
    cart_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("User.user_id"))
    user=relationship("User",back_populates="cart")
class Cartitem(Base):
    __tablename__="Cartitem"
    cart_item_id=Column(Integer,primary_key=True)
    cart_id=Column(Integer,ForeignKey("Cart.cart_id"))
    product_id=Column(Integer,ForeignKey("Product.product_id"))
    quantity=Column(Integer,nullable=False)
    product=relationship("Product",back_populates="cartitem")
    cart=relationship("Cart",back_populates="cartitem")
class Wishlist(Base):
    __tablename__="Wishlist"
    wishlist_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("User.user_id"))
    user=relationship("User",back_populates="wishlist")
class Order(Base):
    __tablename__="Order"
    order_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("User.user_id"))
    amount=Column(Float)
    shipping_address=Column(String)
    payment_status=Column(String)
    order_status=Column(String)
    created_at=Column(DATETIME)
    user=relationship("User",back_populates="orders")
    payment=relationship("Payment",back_populates="order")
    orderitem=relationship("OrderItem",back_populates="order")
class OrderItem(Base):
    __tablename__="OrderItem"
    orderitem_id=Column(Integer,primary_key=True)
    order_id=Column(Integer,ForeignKey("Order.order_id"))
    product_id=Column(Integer,ForeignKey("Product.product_id"))
    quantity=Column(Integer,nullable=False)
    price=Column(Float,nullable=False)
    order=relationship("Order",back_populates="orderitem")
    product=relationship("Product",back_populates="orderitem")
class Coupon(Base):
    __tablename__="Coupon"
    coupon_id=Column(Integer,primary_key=True)
    coupon_code=Column(String,nullable=False)
    discount_percentage=Column(Integer,nullable=False)
    expiry_date=Column(DATETIME,nullable=False)
    minimum_purchase=Column(Float,nullable=False)
class Payment(Base):
    __tablename__="Payment"
    payment_id=Column(Integer,primary_key=True)
    order_id=Column(Integer,ForeignKey("Order.order_id"))
    payment_method=Column(String,nullable=False)
    amount=Column(Float,nullable=False)
    order=relationship("Order",back_populates="payment")
class Review(Base):
    __tablename__="Review"
    review_id=Column(Integer,primary_key=True)
    product_id=Column(Integer,ForeignKey("Product.product_id"))
    user_id=Column(Integer,ForeignKey("User.user_id"))
    rating=Column(Integer)
    review_text=Column(String)
    user=relationship("User",back_populates="reviews")
    product=relationship("Product",back_populates="reviews")