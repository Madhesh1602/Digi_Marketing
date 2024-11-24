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

**Content Tone(s):** {content_tone}

**Content Style(s):** {content_style}

**Audience Prototype(s):** {audience_prototype}

**Special Occasion (if applicable):** {occasion_type}

**Hook(s):** {hooks}

**Language:** {language}

**Word Count (if applicable):** {word_count}


**Content Guidelines:**

* **Maintain a balance between promotional, informative, and engaging content.**  
* **Adopt a {content_tone} tone and a {content_style} style to resonate with the target audience.**  
* **Incorporate the chosen hooks effectively to capture attention.**  
* **Highlight key features and benefits of {product_name} based on the image description.**  
* **Tailor the content to appeal to the defined audience prototype(s): {audience_prototype}.**  
* **If applicable, creatively connect the content to the special occasion ({occasion_type}).**  
* **Ensure the content aligns with the best practices of the selected social media platform ({social_media}).**  

**Deliverables:**

Provide a detailed outline of the {product_name} content. 

**Start with a compelling opening that utilizes the available hooks ({hooks}).**

**Follow the appropriate structure below based on the requested content type ({content_type}).** 

**Example Structure for Video Voiceover Script:**

* **Hook (0-5 seconds):**  
  [Grab attention with {hooks}. Example: Startling statistic, intriguing question, or a humorous scenario related to the product/problem it solves.]  
* **Introduction (5-15 seconds):**  
  [Introduce {business_name} and the problem {product_name} solves. Connect it to the target audience's needs or desires, with an emphasis on the {audience_prototype}.]  
* **Product Showcase (15-45 seconds):**  
  [Highlight the product's key features and benefits in a {content_tone} tone and {content_style} style. Address potential objections (e.g., price, doubts about effectiveness) using examples relatable to the {audience_prototype}.]  
* **Social Proof/Occasion Tie-in (45-60 seconds):**  
  [Incorporate testimonials, user-generated content, or a connection to the special occasion, tailored to the {audience_prototype}.]  
* **Call to Action ({content_duration} seconds):**  
  [Encourage viewers to take the desired action (e.g., visit website, learn more, make a purchase). Offer a limited-time promotion or incentive relevant to the goal.]

**Example Structure for Post Caption:**

* **Hook (Sentence 1):** [Grab attention with {hooks}. Example: Bold statement, question that sparks curiosity, relatable anecdote]
* **Product Introduction (Sentences 2-3):** [ Briefly describe {product_name} and its key benefits. Highlight what makes it unique or desirable.]
* **Features/Benefits (Sentences 4-6):** [Expand on the product's key features and how they address the target audience's needs. Use persuasive language.]
* **Call to Action (Final Sentence(s)):** [Encourage engagement (e.g., "Tag a friend," "Share your thoughts," "Visit our website to learn more").]

Generate content only for the requested content type ({content_type}) and ensure it aligns with the provided guidelines.
"""
