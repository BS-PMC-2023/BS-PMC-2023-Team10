def calculate_customer_satisfaction(survey_responses):
    total_responses = len(survey_responses)
    positive_responses = 0

    for response in survey_responses:
        # Assuming 'satisfaction' is a key in the survey response data
        if response['satisfaction'] >= 4:
            positive_responses += 1

    satisfaction_rate = (positive_responses / total_responses) * 100
    return satisfaction_rate


if __name__ == "__main__":
    survey_responses = [
        {'satisfaction': 5, 'comment': 'Great product!'},
        {'satisfaction': 4, 'comment': 'Good experience.'},
        {'satisfaction': 3, 'comment': 'Average quality.'},
        {'satisfaction': 2, 'comment': 'Needs improvement.'},
        {'satisfaction': 5, 'comment': 'Excellent service!'},
    ]

    satisfaction_rate = calculate_customer_satisfaction(survey_responses)
    print(f"Customer Satisfaction Rate: {satisfaction_rate}%")
