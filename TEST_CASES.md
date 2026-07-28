# Test Cases

This document contains the test scenarios executed to verify the functionality of the AI-Assisted Box Selection System.

---

## Test Case 1: Display Product List

**Objective**

Verify that all products are displayed on the home page.

**Input**

Open the application.

**Expected Result**

The home page should display the list of available products with a **Recommend Box** button.

**Actual Result**

Products were displayed successfully.

**Status**

Passed

---

## Test Case 2: Recommend a Suitable Box

**Objective**

Verify that the system recommends the correct shipping box.

**Input**

Click the **Recommend Box** button for a product.

**Expected Result**

The system should display a suitable shipping box along with its shipping cost.

**Actual Result**

The recommendation page displayed the correct box and shipping cost.

**Status**

Passed

---

## Test Case 3: Product Fits Inside Recommended Box

**Objective**

Verify that the selected box satisfies the product dimensions and weight.

**Input**

Select any available product.

**Expected Result**

The recommended box should have sufficient dimensions and weight capacity.

**Actual Result**

The recommended box satisfied all conditions.

**Status**

 Passed

---

## Test Case 4: Django Admin

**Objective**

Verify that products and shipping boxes can be managed through Django Admin.

**Input**

Login to Django Admin.

**Expected Result**

Products and boxes should be added, edited and deleted successfully.

**Actual Result**

All CRUD operations worked successfully.

**Status**

Passed

---

## Test Case 5: Home Page Accessibility

**Objective**

Verify that the application loads successfully.

**Input**

Open:

```
http://127.0.0.1:8000/
```

**Expected Result**

Home page should load without any errors.

**Actual Result**

Application loaded successfully.

**Status**

Passed

---

## Overall Result

All major functionalities of the application were tested successfully and produced the expected results.