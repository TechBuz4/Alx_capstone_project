# TINASH E-commerce Product API

![E-commerce API](https://img.shields.io/badge/Django-REST%20Framework-blue) 
![Authentication](https://img.shields.io/badge/Auth-JWT-green) 
![Database](https://img.shields.io/badge/Database-SQLite%20%2F%20PostgreSQL-orange)

A robust Django REST Framework API for an e-commerce platform specializing in fashion items (clothes, bags, and shoes). The API supports product management, cart operations, secure authentication, and order processing with role-based access control.

## Table of Contents
- [Features](#key-features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Database Models](#database-models)
- [Search & Filtering](#search--filtering)
- [Future Enhancements](#future-enhancements)

## Key Features

### Product Management
- **Sellers** can:
  - Add new products
  - Update product details (price, description, availability)
  - Delete products from listings
- **Buyers** can:
  - Browse available products
  - View product details

### Cart & Order System
- **Buyers** can:
  - Add/remove items from cart
  - View cart contents
  - Place orders

### User Management
- Role-based access control:
  - Buyers: Manage carts and orders
  - Sellers: Manage product listings
- User registration and profile management

### Search & Filtering
- Search products by name or keywords
- Filter by category (clothing, footwear, accessories)
- Django ORM for efficient queries

## API Endpoints

### Authentication
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/register/` | POST | User registration |
| `/api/login/` | POST | obtain token for login |

### Products
| Endpoint | Method | Description | Permission |
|----------|--------|-------------|------------|
| `/api/products/` | GET | List all products | Any |
| `/api/products/` | POST | Add new product | Seller only |

### Cart
| Endpoint | Method | Description | Permission |
|----------|--------|-------------|------------|
| `/api/cart/` | GET | View cart items | Buyer |
| `/api/cart/add/` | POST | Add to cart | Buyer |
| `/api/cart/<id>/` | DELETE | Remove from cart | Buyer |

### Orders
| Endpoint | Method | Description | Permission |
|----------|--------|-------------|------------|
| `/api/orders/` | GET | List user orders | Buyer |
| `/api/orders/` | POST | Create new order | Buyer |

## Database Models

### Core Models
1. **User** (Extends AbstractUser)
   - username
   - email
   - role (buyer/seller)

2. **Category**
   - name (clothing, footwear, accessories)
   - description

3. **Product**
   - name
   - description
   - price
   - category (FK)
   - seller (FK to User)

4. **CartItem**
   - user (FK)
   - product (FK)
   - quantity

5. **Order**
   - user (FK)
   - products (ManyToMany through OrderItem)
   - total_price
   - status (pending, completed, cancelled)
   - created_at

## Future Enhancements

1. **Payment Integration**
   - Stripe/Paypal payment processing
   - Payment confirmation webhooks

2. **Order Tracking**
   - Shipping status updates
   - Delivery notifications

3. **Product Reviews & Ratings**
   - User feedback system
   - Average rating calculation

4. **Advanced Search**
   - Price range filtering
   - Sorting options (price, popularity)

5. **Admin Dashboard**
   - Sales analytics
   - Inventory management

6. **Production Deployment**
   - PostgreSQL database
   - Docker containerization
   - CI/CD pipeline

---

**Contributors**: [Busayo Ososanwo]  
