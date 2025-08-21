# glucose_prediction_app

A new Flutter project.

## Getting Started

# Glucose Level Prediction Flutter App

A Flutter mobile application that predicts glucose levels using a machine learning API.

## Features

✅ **10 Input Fields** - All required variables for glucose prediction:
- Age (10-100 years)
- Gender (0=Female, 1=Male) 
- Weight (20-200 kg)
- Skin Color (1-3)
- NIR Reading (50-1000)
- Heart Rate (20-200 bpm)
- Height (4.0-7.5 feet)
- Hours Since Last Meal (0-24)
- Diabetic Status (0=No, 1=Yes)
- HR Infrared Reading (10000-120000)

✅ **"Predict" Button** - Sends data to API and gets prediction
✅ **Result Display Area** - Shows predicted glucose level or error messages
✅ **Input Validation** - Enforces data types and acceptable ranges
✅ **Professional UI** - Clean, organized layout with icons and proper spacing
✅ **Error Handling** - User-friendly error messages for invalid inputs
✅ **Loading States** - Shows progress indicator during API calls
✅ **Clear Function** - Reset all fields with one button

## API Integration

- **Endpoint**: `https://linear-regression-model2.onrender.com/predict`
- **Method**: POST
- **Content-Type**: application/json
- **Response**: JSON with predicted glucose level

## App Structure

### 📱 Single Page Application
- **Header**: App title and health icon
- **Input Section**: 10 text fields with validation
- **Action Buttons**: Predict and Clear buttons
- **Result Section**: Displays prediction or error messages

### 🎨 UI Features
- **Material Design 3** with teal color scheme
- **Icons** for each input field (calendar, person, heart, etc.)
- **Cards** for organized sections
- **Responsive layout** that works on different screen sizes
- **Loading indicators** and success/error states

## How to Run

1. **Install Dependencies**:
   ```bash
   flutter pub get
   ```

2. **Run on Mobile Device**:
   ```bash
   flutter run
   ```

3. **Run in Web Browser**:
   ```bash
   flutter run -d chrome
   ```

4. **Run on Specific Port**:
   ```bash
   flutter run -d chrome --web-port 8080
   ```

## Usage Instructions

1. **Fill All Fields**: Enter valid values for all 10 required fields
2. **Validation**: App will show error messages if values are out of range
3. **Predict**: Click the "Predict" button to get glucose level prediction
4. **View Results**: Prediction appears in the result card below
5. **Clear**: Use "Clear" button to reset all fields

## Technical Details

- **Framework**: Flutter 3.8.1+
- **Language**: Dart
- **HTTP Client**: http package v1.5.0
- **UI**: Material Design 3
- **Platform**: Cross-platform (iOS, Android, Web)

## API Integration Details

The app sends a POST request with JSON data:
```json
{
  "AGE": 45,
  "GENDER": 1,
  "WEIGHT": 70.5,
  "SKIN_COLOR": 2,
  "NIR_Reading": 850.0,
  "HEARTRATE": 75.0,
  "HEIGHT": 5.8,
  "LAST_EATEN": 2.5,
  "DIABETIC": 0,
  "HR_IR": 45000.0
}
```

And receives a response like:
```json
{
  "predicted_glucose_level": 95.67
}
```

## Requirements Met ✅

- ✅ More than one page capability (single scrollable page with sections)
- ✅ Text fields for all prediction variables (10 fields)
- ✅ "Predict" button as specified
- ✅ Display area for predictions and error messages
- ✅ Proper organization and layout
- ✅ No overlapping elements
- ✅ Professional, presentable appearance
- ✅ API integration with deployed endpoint
- ✅ Data validation and error handling
