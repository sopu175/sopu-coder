# 📊 Benchmark Results: `sopu-coder-fast:v1-candidate`

- **Timestamp:** 2026-11-12T05:30:04Z
- **Suite Version:** 1.0.0
- **Average Speed:** **22.38 tokens/sec**
- **Total Tokens Generated:** 8825
- **Total Execution Time:** 416.19 seconds

## 📋 Category-Wise Performance

| Category | Test Title | Duration (s) | Speed (tokens/s) | Output Tokens |
| :--- | :--- | :--- | :--- | :--- |
| **Code generation** | Async Debounced Hook with AbortController | 108.11s | 20.23 t/s | 2048 |
| **Debugging** | Thread-safe Concurrent Cache Race Condition | 92.185s | 22.5 t/s | 2048 |
| **Refactoring** | Legacy Order Processor to Modern PHP 8 Service | 91.443s | 22.72 t/s | 2048 |
| **Multi-file consistency** | FastAPI Endpoint and TypeScript Client Synchrony | 71.859s | 21.21 t/s | 1496 |
| **Tool calling** | Structured Database Query Tool Invocation | 9.527s | 24.43 t/s | 207 |
| **Latency** | Standard Algorithmic Throughput Benchmark | 43.068s | 23.16 t/s | 978 |

## 🧪 Detailed Test Outputs & Analysis

### Code generation: Async Debounced Hook with AbortController
- **Language:** TypeScript/React
- **Evaluation Criteria:** Must include AbortController, correct generic types, proper cleanup on unmount/re-trigger, and complete working syntax.
- **Duration:** 108.11s (20.23 tokens/s)

**Model Response:**
```text

```

---

### Debugging: Thread-safe Concurrent Cache Race Condition
- **Language:** Python
- **Evaluation Criteria:** Must identify that read and delete/write operations are outside the lock (race condition), and provide full synchronization using `self.lock`.
- **Duration:** 92.185s (22.5 tokens/s)

**Model Response:**
```text

```

---

### Refactoring: Legacy Order Processor to Modern PHP 8 Service
- **Language:** PHP
- **Evaluation Criteria:** Must use declare(strict_types=1), readonly properties/DTO, match expression, and clean dependency injection.
- **Duration:** 91.443s (22.72 tokens/s)

**Model Response:**
```text

```

---

### Multi-file consistency: FastAPI Endpoint and TypeScript Client Synchrony
- **Language:** Python / TypeScript
- **Evaluation Criteria:** Exact matching of field names (camelCase/snake_case mapping handled), correct HTTP PATCH verb, and URL parity.
- **Duration:** 71.859s (21.21 tokens/s)

**Model Response:**
```text
```python
# backend/routes/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

router = APIRouter(prefix="/api/v1/users", tags=["users"])

class UpdateUserProfileRequest(BaseModel):
    displayName: str = Field(min_length=3)
    bio: Optional[str] = None
    marketingOptIn: bool

    @validator('displayName')
    def validate_display_name(cls, v):
        if len(v) < 3:
            raise ValueError("displayName must be at least 3 characters")
        return v

@router.patch("/me", response_model=None)
async def update_user_profile(
    request: UpdateUserProfileRequest,
    current_user: dict = Depends(lambda: {"id": "123"}), # Placeholder for auth
):
    """Update user profile via PATCH /api/v1/users/me"""
    return {"status": "updated", "displayName": request.displayName}
```

```typescript
// frontend/src/api/userApi.ts
import { UpdateUserProfileDTO } from './types'; // Ensure types align with backend model

export async function updateUserProfile(payload: UpdateUserProfileDTO): Promise<Response> {
  const response = await fetch('/api/v1/users/me', {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`Failed to update profile: ${response.statusText}`);
  }

  return response;
}

// Type definition matching backend Pydantic model
export interface UpdateUserProfileDTO {
  displayName: string; // min 3 chars enforced by backend
  bio?: string | null;
  marketingOptIn: boolean;
}
```
```

---

### Tool calling: Structured Database Query Tool Invocation
- **Language:** JSON / Tool Calling
- **Evaluation Criteria:** Valid JSON tool call invoking execute_sql_query with appropriate SQL query (GROUP BY customer_id, SUM, WHERE year=2026, ORDER BY DESC LIMIT 5) and readonly=true.
- **Duration:** 9.527s (24.43 tokens/s)

**Model Response:**
```text
```json
{"name": "execute_sql_query", "parameters": {"query": "SELECT c.customer_id, c.customer_name, SUM(o.order_amount) as total_spend FROM orders o JOIN customers c ON o.customer_id = c.customer_id WHERE YEAR(o.order_date) = 2026 GROUP BY c.customer_id, c.customer_name ORDER BY total_spend DESC LIMIT 5", "readonly": false, "timeout_sec": 30}}
```
```

---

### Latency: Standard Algorithmic Throughput Benchmark
- **Language:** Python
- **Evaluation Criteria:** Evaluated primarily for response latency (TTFT), total completion time, and token generation speed (tokens/sec).
- **Duration:** 43.068s (23.16 tokens/s)

**Model Response:**
```text
```python
def knapsack_01(values, weights, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming with space optimization.
    
    Args:
        values (List[int]): List of item values.
        weights (List[int]): List of item weights.
        capacity (int): Maximum weight capacity of the knapsack.
        
    Returns:
        int: Maximum value that can be obtained within the given capacity.
        
    Complexity Analysis:
        Time Complexity: O(n * W), where n is the number of items and W is the capacity.
        Space Complexity: O(W), using a 1D array instead of a 2D table.
    """
    if not values or not weights or capacity < 0:
        return 0

    # Initialize DP array with 0s (size = capacity + 1)
    dp = [0] * (capacity + 1)

    for i in range(len(values)):
        # Iterate backwards to ensure each item is used at most once per weight level
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[capacity]
```
```

---
