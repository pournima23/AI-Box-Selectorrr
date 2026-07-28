# Test Output

## Testing Summary

After completing the development of the AI-Assisted Box Selection System, I tested the application to verify that all major features were working correctly. The testing was performed on the local development server using sample products and shipping boxes added through the Django Admin panel.

---

## Test Environment

| Component | Details |
|----------|---------|
| Operating System | Windows 11 |
| Programming Language | Python 3 |
| Framework | Django |
| Database | SQLite |
| IDE | Visual Studio Code |
| Browser | Google Chrome |

---

## Test 1 - Home Page

### Action Performed

Opened the application using:

```
http://127.0.0.1:8000/
```

### Expected Result

The application should display the list of available products.

### Actual Result

The home page loaded successfully and all products were displayed correctly.

**Status:** Passed

---

## Test 2 - Box Recommendation

### Action Performed

Clicked the **Recommend Box** button for a product.

### Expected Result

The application should recommend the most suitable shipping box and display its shipping cost.

### Actual Result

The recommendation page displayed the correct shipping box along with its shipping cost.

**Status:** Passed

---

## Test 3 - Django Admin

### Action Performed

Logged into the Django Admin panel and added products and shipping boxes.

### Expected Result

The data should be stored successfully and become available in the application.

### Actual Result

Products and shipping boxes were added successfully and appeared correctly on the home page.

**Status:** Passed

---

## Test 4 - Recommendation Logic

### Action Performed

Tested different products having different dimensions and weights.

### Expected Result

The application should compare the product with the available shipping boxes and recommend a suitable one.

### Actual Result

The recommendation logic worked correctly and selected an appropriate shipping box based on the product dimensions and weight.

**Status:** Passed

---

## Final Result

All planned test cases were executed successfully. The application behaved as expected and no functional issues were observed during testing. The box recommendation feature, Django Admin operations, and user interface were verified successfully.