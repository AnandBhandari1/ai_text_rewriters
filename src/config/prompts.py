# Configuration for predefined prompts
PROMPTS = {
    'Grammar Improver': {
        'title': 'Grammar Improvement',
        'content': 'Your task is to act as an English grammar and style assistant. When I provide you with text, you should only rewrite or correct the text while preserving its intended meaning. Do not add any explanations, comments, or other responses—only provide the rewritten version of the text.'
    },
    "Slack Chat Responder": {
        'title': 'Slack Chat Responder',
        'content': 'Act as a Slack chatbot. Rewrite the following text to be suitable for responding to Slack messages. Use clear, concise language, and maintain a professional tone.'
    },
    "Slack chat summarizer": {
        'title': 'Slack Chat Summarizer',
        'content': 'Act as a Slack chatbot. Rewrite the following text to be suitable for summarizing Slack messages. Use clear, concise language. Write the key points of the text.'
    },
    "Slack Chat Analyzer": {
        'title': 'Slack Chat Analyzer',
        'content': 'Act as a Slack chatbot. Analyze the following text and provide insights into its content. Find if there are any TODOs, tasks, or important points. Find if any notion task needed to create then write it. Find if there are any important links or resources. Do not write any explanations, comments, or other responses. Only provide the analysis.'
    },
    'Notion Task Writer': {
        'title': 'Notion Task Creation',
        'content': 'Act as a task creator for Notion. Rewrite the following text to be suitable for creating tasks in Notion. Use clear, concise language, and maintain a professional tone.'
    },
    'Story Rewriter': {
        'title': 'Creative Story Enhancement',
        'content': 'Act as a creative writer. Rewrite the following text to make it more engaging and story-like, while keeping the main elements and meaning intact. Focus on narrative flow and descriptive language.'
    },
    'Technical Writer': {
        'title': 'Technical Documentation',
        'content': 'Act as a technical writer. Rewrite the following text to be clear, precise, and suitable for technical documentation. Use professional terminology while maintaining clarity.'
    },
    'Simplifier': {
        'title': 'Text Simplification',
        'content': 'Your task is to simplify the following text. Make it easier to understand while keeping the main message. Use clear, straightforward language and shorter sentences.'
    },
    'Business Writer': {
        'title': 'Business Communication',
        'content': 'Act as a business writing expert. Rewrite the following text to be professional, concise, and suitable for business communication. Use appropriate business terminology and maintain a formal tone.'
    },
    'Academic Style': {
        'title': 'Academic Writing',
        'content': 'Act as an academic writing expert. Rewrite the following text to follow academic writing standards. Use scholarly language, maintain objectivity, and ensure formal academic tone.'
    },
    'Code Explainer': {
        'title': 'Code Explanation',
        'content': 'Act as a programming tutor. Explain the following code in simple terms, providing insights into its logic and functionality. Use clear, beginner-friendly language.'
    },
    'Bug Finder': {
        'title': 'Bug Finding',
        'content': 'Your task is to act as a debugging assistant. Analyze the following code to identify any errors or inefficiencies. Suggest fixes or improvements without altering the core functionality.'
    },
    'Code Optimizer': {
        'title': 'Code Optimization',
        'content': 'Act as a code optimizer. Rewrite the following code to make it more efficient and clean. Use best practices and optimize for performance and readability.'
    },
    'Logic Simplifier': {
        'title': 'Logic Simplification',
        'content': 'Your task is to simplify the logic in the provided code. Make it easier to understand and maintain while preserving its functionality.'
    },
    'API Documenter': {
        'title': 'API Documentation',
        'content': 'Act as an API documentation specialist. Draft clear and concise documentation for the following code. Include details such as function parameters, return values, and examples.'
    },
    'Algorithm Designer': {
        'title': 'Algorithm Design',
        'content': 'Act as an algorithm designer. Create or refine the algorithm for the following problem. Ensure clarity, efficiency, and proper structure in your design.'
    },
    'Database Designer': {
        'title': 'Database Design',
        'content': 'Act as a database schema expert. Design or optimize the database schema for the provided requirements. Use proper normalization and best practices in database design.'
    },
    'UX Enhancer': {
        'title': 'UX Enhancement',
        'content': 'Your task is to act as a UX expert. Review the provided interface or functionality and suggest improvements for better user experience. Focus on usability and accessibility.'
    },
    'Security Advisor': {
        'title': 'Security Advice',
        'content': 'Act as a security advisor. Analyze the provided code or application for potential vulnerabilities. Suggest improvements or solutions to enhance security.'
    },
    'Language Converter': {
        'title': 'Language Conversion',
        'content': 'Your task is to convert the provided code from one programming language to another. Ensure the functionality and logic remain intact while using idiomatic constructs of the target language.'
    },
    'Trending Keywords': {
        'title': 'Trending Keywords',
        'content': 'What are some of the top long-tail keywords currently trending in the X niche?'
    },
    'Blog Post Outline': {
        'title': 'Blog Post Outline',
        'content': 'Make an outline for a blog post about XYZ using related keywords based on Google search data.'
    },
    'Blog Post Introduction': {
        'title': 'Blog Post Introduction',
        'content': 'Write an introduction to a blog post about XYZ.'
    },
    'Full Blog Post': {
        'title': 'Full Blog Post',
        'content': 'Write a blog post about XYZ. (This is good instruction for each section of your blog post to get longer content.)'
    },
    'Provide Examples': {
        'title': 'Provide Examples',
        'content': 'What’s a good example of XYZ?'
    },
    'Step-by-Step Guide': {
        'title': 'Step-by-Step Guide',
        'content': 'Give me a step-by-step process for XYZ.'
    },
    'Pros and Cons Table': {
        'title': 'Pros and Cons Table',
        'content': 'What are the pros and cons of XYZ? Present the information in a table.'
    },
    'Personal Example': {
        'title': 'Personal Example',
        'content': 'Give me a personal example of someone using X product for Y.'
    },
    'Storytelling': {
        'title': 'Storytelling',
        'content': 'Tell a personal story about X.'
    },
    'Keyword Integration': {
        'title': 'Keyword Integration',
        'content': 'Write a blog post about X using this keyword (insert keyword) several times naturally throughout the content.'
    },
    'FAQs': {
        'title': 'FAQs',
        'content': 'Give me a list of the most frequently asked questions about X.'
    },
    'SEO-Friendly Content': {
        'title': 'SEO-Friendly Content',
        'content': 'What is the best approach for creating SEO-friendly content in X niche?'
    },
    'Key Points and Stats': {
        'title': 'Key Points and Stats',
        'content': 'How can highlighting key points and stats make a blog post more effective?'
    },
    'Repurpose Content': {
        'title': 'Repurpose Content',
        'content': 'What are some creative ways to repurpose old blog posts?'
    },
    'Targeting Audiences': {
        'title': 'Targeting Audiences',
        'content': 'How can bloggers effectively target specific audiences through their content?'
    },
    'Headline Tips': {
        'title': 'Headline Tips',
        'content': 'What tips and tricks can be used to write high-converting blog headlines?'
    },
    'Shareable Content': {
        'title': 'Shareable Content',
        'content': 'How can bloggers ensure they produce quality content that is easily sharable?'
    },
    'Research Topics': {
        'title': 'Research Topics',
        'content': 'What questions should be asked when researching topics for a blog post in X niche?'
    },
    'Multimedia Content': {
        'title': 'Multimedia Content',
        'content': 'How can audio and video content be leveraged to increase traffic to blogs?'
    },
    'Visual Impact': {
        'title': 'Visual Impact',
        'content': 'How do influencers, industry leaders, and top bloggers use visuals to enhance their content’s impact on readers?'
    },
    'Blogging Benefits': {
        'title': 'Blogging Benefits',
        'content': 'How does blogging help increase brand awareness and generate leads for businesses in X niche?'
    },
    'Graphic Design': {
        'title': 'Graphic Design',
        'content': 'Are there any techniques or shortcuts for creating professional graphics quickly for blogs?'
    },
    'Build Relationships': {
        'title': 'Build Relationships',
        'content': 'What strategies can new bloggers use to create meaningful relationships with readers online?'
    },
    'Interactive Experiences': {
        'title': 'Interactive Experiences',
        'content': 'What are some interesting ideas for creating unique interactive experiences through blogging?'
    },
    'Content Focus': {
        'title': 'Content Focus',
        'content': 'Should bloggers focus more on quantity or quality when it comes to producing content in X niche?'
    },
    'Infographics': {
        'title': 'Infographics',
        'content': 'Are there any clever ways of incorporating infographics into blog posts while still retaining the readability and usability of the post itself?'
    },
    'Social Media': {
        'title': 'Social Media',
        'content': 'Which types of social media posts lead to increased engagement with blog content across various platforms?'
    },
    'Google Ranking': {
        'title': 'Google Ranking',
        'content': 'What topics should I include in my blog post to rank on Google for X keyword?'
    }
}
