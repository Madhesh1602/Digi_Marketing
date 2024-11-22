SHORT_DESCRIPTION_TEMPLATE = """Give a short concise description of the given image.
This description will be used to market the product so make sure to include all the key details visible in the image.
Please do not hallucinate but only include the details that are visible in the image.
"""

LONG_DESCRIPTION_TEMPLATE = """
Act as a social media strategist for {business_name}, a {target_customer} business, targeting people aged {min_age}-{max_age} in {region}. 
Generate a {content_duration} second {content_type} for {product_name}.

**Product Description:**
{image_description} 

**Social Media Platform:** {social_media}

**Content Goal(s):** {content_goal}

**Special Occasion (if applicable):** {occasion_type}

**Hook(s):** {hooks}

**Language:** {language}

**Word Count (if applicable):** {word_count}


**Content Guidelines:**

* **Maintain a balance between promotional, informative, and engaging content.** 
* **Incorporate the chosen hooks effectively to capture attention.**
* **Tailor the language and tone to resonate with the target audience's age and cultural context in {region}.**
* **Highlight key features and benefits of {product_name} based on the image description.**
* **If applicable, creatively connect the content to the special occasion ({occasion_type}).**
* **Ensure the content aligns with the chosen social media platform's best practices.** 

**Deliverables:**

Provide a detailed outline of the {product_name} content. 

**Start with a compelling opening that utilizes the available hooks ({hooks}).**

**Follow the appropriate structure below based on the requested content type ({content_type}).** 

**Example Structure for Video Voiceover Script:**

* **Hook (0-5 seconds):** [Grab attention with {hooks}. Example: Startling statistic, intriguing question, humorous scenario related to the product/problem it solves]
* **Introduction (5-15 seconds):** [ Briefly introduce {business_name} and the problem {product_name} solves. Connect to the target audience's needs/desires.]
* **Product Showcase (15-45 seconds):** [Highlight key features and benefits of {product_name} using vivid language and visuals from the image description.  Address potential objections (e.g., price, doubts about effectiveness).]
* **Social Proof/Occasion Tie-in (45-60 seconds):**  [If applicable, include testimonials, user-generated content, or connect the product to the special occasion. ]
* **Call to Action (60-{content_duration} seconds):** [Encourage viewers to take the desired action (visit website, learn more, make a purchase). Offer a limited-time promotion or incentive if relevant to the goal.] 

**Example Structure for Post Caption:**

* **Hook (Sentence 1):** [Grab attention with {hooks}. Example: Bold statement, question that sparks curiosity, relatable anecdote]
* **Product Introduction (Sentences 2-3):** [ Briefly describe {product_name} and its key benefits. Highlight what makes it unique or desirable.]
* **Features/Benefits (Sentences 4-6):** [Expand on the product's key features and how they address the target audience's needs. Use persuasive language.]
* **Call to Action (Final Sentence(s)):** [Encourage engagement (e.g., "Tag a friend," "Share your thoughts," "Visit our website to learn more").]

Generate content only for the requested content type ({content_type}) and ensure it aligns with the provided guidelines.
"""
