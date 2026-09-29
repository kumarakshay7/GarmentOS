# GarmentOS Project Plan

## MVP modules

1. Authentication and user roles
2. Dashboard
3. Product master and variants
4. Barcode / QR support
5. Inventory and stock movements
6. Suppliers and purchases
7. Customers
8. POS sales
9. Payments
10. Digital invoices
11. Returns and exchanges
12. Sales, inventory, and profit reports

## Core business flow

Supplier -> Purchase -> Stock In -> Product Variant -> POS Scan -> Sale -> Payment -> Invoice -> Stock Out

Returns / Exchange:
Invoice -> Scan Invoice QR or search invoice -> Select item -> Return / Exchange -> Stock Movement -> New receipt

## Design principles

- Product variants are first-class records: size + colour + SKU + barcode.
- Inventory changes are recorded as stock movements.
- Sales and purchases are immutable business transactions; corrections use adjustments, returns, or cancellation workflows.
- User permissions are enforced on the backend.
- Secrets are stored in environment variables, never in source code.
- The initial system is designed for a small/medium retail garment shop and can later support multiple stores.
