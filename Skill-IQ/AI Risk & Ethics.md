# AI Risk & Ethics

1. You are reviewing model outcomes for two subgroups in a dataset. Each subgroup shows the same true positive rate and false positive rate. Based on these results, what can you conclude?

You have achieved equalized odds and no bias is indicated based on this information.

2. You are analyzing model outputs for different subgroups in a dataset to determine whether the model produces consistent results across those groups. Which analysis can be used to detect imbalances in these outcomes?

Use disparity analysis to identify the different outcomes and compare them to detect bias.

3. You are implementing an AI system based on user data. Considering the threat that data leakage poses, what implementations can you introduce into testing that can help track if personal data can be reconstructed from the model?

Perform tests for membership inference to determine the confidence in predictions for specific data.

4. You do data analysis for a bank and are investigating the history of loans they have accepted and rejected. You are interested in finding out if there are certain features such as locality or credit score that are disproportionately affecting data model outcomes. What would be an effective way to accomplish this?

Implement a technique such as SHAP or LIME to study feature importance analysis.

5. Your organization uses an automated employment decision tool that falls under the scope of New York City (NYC) Local Law 144. According to the law, what requirement applies to this tool?

The tool must undergo an annual bias audit, and a summary of the audit must be made publicly available.

6. You have been tasked with designing an AI system built on user data. To ensure user privacy using federated learning, how should the system handle data?

Users would have access to their own personal data on their devices, and central servers would only receive model updates instead of the raw data.

7. You have deployed an AI agent that handles dissatisfied-customer inquiries and sometimes nudges users toward accepting a less favorable refund or a pricier alternative. There is no evidence of subliminal/deceptive techniques or exploitation of vulnerable groups, nor of significant harm. Under the EU AI Act, what risk level applies?

Limited risk

8. Your company developed an AI model for detecting cancer from CT scans, achieving a 98% accuracy rate—the highest among the last four models delivered to a hospital. However, doctors observe that the new model misses at least 15% of early-stage cancer cases. What steps do you take during model validation to address this issue?

Prioritize recall over precision.

9. You employ a recurrent neural network (RNN) to develop an AI model for sentence completion. To understand how the model makes decisions, you apply Gradient-weighted Class Activation Mapping (Grad-CAM) to highlight token importance within the network. However, this approach proves ineffective. Why?

Grad-CAM works best with a convolutional layer to highlight image regions.

10. You develop a large language model (LLM) that suggests similar clothing items for users in region A, achieving a 95% accuracy rate. After deploying it in region B, the accuracy drops to 70%. You use an AI monitoring tool to detect changes in model behavior, but no alerts are triggered despite changes in input features. Why?

Alerts were not properly configured in the monitoring system.

11. You are training an AI model to align with human values through reinforcement learning from human feedback (RLHF). Your model has achieved the desired level of human values, and you are regularly conducting audits to ensure consistency. What improvements can you make to mitigate misalignments with the data and ensure human oversight and transparency?

Enhance AI interpretability and implement rule-based filters.

12. You deploy a large language model to detect online fraudsters. However, these fraudsters frequently adapt their tactics, which can reduce your model's accuracy over time. What steps will you take when the error rate increases significantly after deploying your initial model?

Retrain your large language model.

13. Your organization has recently appointed you as the head of their lending department. Upon taking charge, you observe that your department relies heavily on AI systems for real-time fraud detection and optimizing customers' investment strategies. Given the significant benefits AI offers, why should you consider reducing this dependency?

It may lead to unfair lending practices.

14. You have completed the processing phase of a model and are evaluating the output. You observe that the positive prediction rate differs across subgroups within the dataset, and you want to adjust the model so the subgroup prediction rates are more consistent. Which strategy can be used to modify the model’s outputs?

Thresholding Adjustment

15. Your team has developed a deep learning AI model utilizing convolutional neural networks to differentiate between class A and class B images. While your customers are satisfied with its performance, they seek an explanation for how the AI arrives at its decisions. However, your team lacks familiarity with explaining deep learning model decisions. As the team leader, what guidance can you provide to help them address this challenge?

Use gradient-weighted class activation mapping to highlight important image regions.

16. You are in the post-processing phase of a loan approval data model that determines who is eligible for a car loan. During investigation of the data analysis, you discover that the true positive rate (TPR) is higher for certain groups than others, indicating that there may be some bias in the data. How would applying Calibrated Equalized Odds help mitigate this issue?

It would adjust the model so that all subgroups have similar true positive and false positive rates.

17. A team of scientists has developed a large language model (LLM) to identify qualified candidates for the position of marketing manager. You adopt their model and apply it to choose the most suitable candidate from a pool of five males and ten females. After using the model to hire three managers, all selected candidates turn out to be male. What factors could account for this outcome if it was not a coincidence?

The model has not undergone a fairness audit using tools such as Fairlearn.

18. Your team develops an AI model that uses a support vector machine (SVM) to make binary decisions. To improve explainability while keeping the rest of the process the same, you consider replacing the SVM with a decision tree. What benefit does this change provide?

You can provide explanation for both models' decisions. 

19. How does reinforcement learning from human feedback (RLHF) enhance the correlation between AI models and humans?

It incorporates human preferences into the AI training model.

20. You leverage AI algorithms to automate your trading setup and generate new trading strategies. One of your algorithms has proven effective in the past 2 years and thus operates on a subscription model, attracting over a million users. However, a recent black swan event led to a substantial loss of your subscribers' wealth. Why did your AI algorithm fail to anticipate this event?

The algorithm failed to generalize anomalies and overfitted to past patterns.
