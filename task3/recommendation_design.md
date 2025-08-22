## 1. Proposal

We want to surface 3--5 "Customers also bought/viewed" items on each
product page.\

## Hybrid Mode Recommended
-   Combine both approaches.
-   If user/product has sufficient history → collaborative filtering.
-   Else fallback to content-based similarity.
- 
#### Content-Based Filtering

-   Uses product features (title, description, tags, category).
-   Works even for new users (no history needed).
-   Pros: Simple, interpretable.
-   Cons: Cannot capture user co-purchase behavior.

#### Collaborative Filtering

-   Based on user-product interactions (purchases, views).
-   "Users who bought X also bought Y".
-   Pros: Captures behavioral patterns.
-   Cons: Cold-start problem (new product or new user).
-

------------------------------------------------------------------------

## 2. Data Sources & Features

-   **Orders data**: product_id, user_id, timestamp (for collaborative
    filtering).
-   **Page views**: product_id, user_id, timestamp.
-   **Product metadata**: title, description, tags, category, price.

------------------------------------------------------------------------

## 3. Implementation Plan

### Data Preparation

1.  Collect product catalog (Using DB directly recommended).
2.  Extract features (title, description embeddings, category tags).
3.  Gather historical transactions and page views.

### Modeling

-   **Content-based**: generate embeddings (OpenAI or
    Sentence-BERT) → cosine similarity.
-   **Collaborative filtering**: build user-item matrix, apply ALS or
    nearest neighbors.
-   **Hybrid**: weighted combination of both.

### Serving

-   Expose API endpoint: `/{product_id}/recommendations`.
-   Return 3--5 recommended product IDs with metadata.

------------------------------------------------------------------------

## 4. KPIs

-   **CTR (Click-Through Rate)**: % of users clicking recommended items.
-   **Conversion Rate**: % of users purchasing recommended items.
-   **Diversity**: measure of variety in recommended products.
-   **Latency**: must be \<200ms per request.

------------------------------------------------------------------------

## 5. Prioritization & Timeline (Estimation)

-   Data Collection → 2 day\
-   Content-based prototype → 2 day\
-   Collaborative filtering prototype → 3 days\
-   Hybrid integration → 1 day\
-   API deployment & testing → 2 day

Total: 10 work days (70 hours)

------------------------------------------------------------------------
