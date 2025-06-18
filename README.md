# Traditional Bread Store Inventory System

**Capstone Project Module 1 – Muhammad Nafi Adziq (Data Science Class)**  
**Theme:** Sales Management in a Traditional Bakery Store  

---

## Overview

This Python-based application simulates a basic inventory and transaction system for a traditional bread store. It supports operations like managing inventory, updating product details, processing sales, and tracking revenue from sold items.

---

## Features

- **View Items List**: Display all items in inventory with details like name, stock, price, origin, flavor, ID, and quantity sold.
- **Add New Item**: Add new bread items with automatic ID generation.
- **Remove Item**: Remove any item using its index.
- **Update Item**: Update specific attributes or the entire data of an existing item.
- **Buy Item**: Simulate a purchase by selecting items, specifying quantity, and processing payment.
- **Revenue Tracking**: Track revenue from each transaction.

---

## Data Model

Data is stored using parallel lists:

- `itemName`: List of bread names.
- `itemQty`: Quantity available.
- `itemPrice`: Price per unit.
- `itemOriginialProducer`: Country of origin.
- `itemFlavour`: Flavour.
- `itemID`: Unique ID.
- `itemSold`: Units sold.

---

## Installation

Only needs python(3.13.5) for running.
