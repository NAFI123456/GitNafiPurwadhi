# Traditional Bread Store Inventory System

**Capstone Project 1– Muhammad Nafi Adziq**  
**Theme:** Sales Management in a Traditional Bakery Store  

---

## Overview

This Python-based application simulates a basic inventory and transaction system for a traditional bread store. It supports operations like managing inventory, updating product details, processing sales, and tracking revenue from sold items.

**Benefits**
-- Eases business decision making.
-- Improved data accuracy and consistency
-- Streamlined data management processes

**Target User**
Business owners.

---

## Features

- **View Items List**: Display all items in inventory with details like name, stock, price, origin, flavor, ID, and quantity sold.
- **Add New Item**: Add new bread items with automatic ID generation.
- **Remove Item**: Remove any item using its index.
- **Update Item**: Update specific attributes or the entire data of an existing item.
- **Buy Item**: Simulate a purchase by selecting items, specifying quantity, and processing payment.
- **Revenue Tracking**: Track revenue from each transaction.

---

## Installation

Only needs python(3.13.5) for running.

---

## usage

1.**Run Program**
2. CRUD Operation (Choose a Prompt With Index Number)
- Create: Add a new item record, for example; item name, item producer, etc.
- Read: Search and retrieve customer information by name, ID, or other relevant criteria.
- Update: Modify customer details, such as updating their address or contact details.
- Delete: Remove a customer record from the system (with appropriate authorization, if applicable).
- Buy: Simulates buying an item.

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


