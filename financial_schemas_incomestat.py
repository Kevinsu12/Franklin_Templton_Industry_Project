from typing import Optional
from pydantic import BaseModel, Field

class IncomeStatement_2024_25(BaseModel):

    # ─── OPERATING REVENUES ──────────────────────────────────────
    gross_tuition_revenue: Optional[int] = Field(
        description="Gross tuition revenue before financial aid for 2024–2025. "
                    "Look for labels like 'Gross Tuition and Fees'. Exclude net tuition or post-discounted amounts."
    )

    financial_aid: Optional[int] = Field(
        description="Institutional financial aid or tuition discounts for 2024–2025. "
                    "Labeled 'Scholarships', 'Grants', or 'Financial Aid'. Do not include federal aid."
    )

    net_tuition_revenue: Optional[int] = Field(
        description="Tuition revenue net of financial aid for 2024–2025. "
                    "Must be explicitly labeled as 'Net Tuition Revenue' or equivalent. Do not compute manually."
    )

    federal_grants_contracts: Optional[int] = Field(
        description="Federal operating grants and contracts for 2024–2025. "
                    "Look for 'Federal Grants & Contracts' in operating revenue section. Exclude capital grants."
    )

    state_local_grants_contracts: Optional[int] = Field(
        description="State or local government operating grants and contracts for 2024–2025. "
                    "Exclude restricted or capital-only support."
    )

    government_grants_contracts_total: Optional[int] = Field(
        description="Combined federal, state, and local grants/contracts for 2024–2025, if labeled as a total. "
                    "Do not compute unless explicitly stated."
    )

    state_appropriations: Optional[int] = Field(
        description="Base state funding or appropriations for 2024–2025. "
                    "Exclude capital-specific appropriations unless labeled as operating."
    )

    private_gifts_grants_contracts: Optional[int] = Field(
        description="Private support for operations for 2024–2025. "
                    "Includes gifts, contributions, grants. Must be unrestricted or labeled for current use."
    )

    total_gifts_contracts_other_support: Optional[int] = Field(
        description="Total of all gifts, grants, and other support for operations for 2024–2025. "
                    "Only extract if explicitly labeled as total. Do not sum manually."
    )

    private_gifts_with_donor_restrictions: Optional[int] = Field(
        description="Gifts or grants with donor restrictions for time or purpose, applicable to 2024–2025. "
                    "Must be clearly labeled. Do not infer from general private support."
    )

    investment_income_operations: Optional[int] = Field(
        description="Investment income available for operational use during 2024–2025. "
                    "May be labeled 'Operating Investment Income'. Exclude restricted or unrealized returns."
    )

    other_investment_income: Optional[int] = Field(
        description="Other investment income not otherwise categorized, if labeled separately. "
                    "Include interest, pooled funds, etc., only if labeled clearly."
    )

    investment_income_total: Optional[int] = Field(
        description="Total investment income (dividends + interest) for 2024–2025. "
                    "Exclude gains/losses unless stated as included."
    )

    realized_gains_losses: Optional[int] = Field(
        description="Realized gains or losses on investments for 2024–2025. "
                    "Include only if specifically labeled. Do not combine with unrealized."
    )

    unrealized_gains_losses: Optional[int] = Field(
        description="Unrealized gains or losses for 2024–2025, typically due to fair value changes. "
                    "Must be labeled 'Unrealized'."
    )

    realized_unrealized_gains_combined: Optional[int] = Field(
        description="Combined realized/unrealized gains or losses, if labeled together. "
                    "Exclude if the document breaks them out separately."
    )

    total_operating_investment_return: Optional[int] = Field(
        description="Total investment return used for operations, including realized/unrealized, for 2024–2025. "
                    "Only extract if labeled as 'Operating Investment Return' or equivalent."
    )

    investment_income_with_donor_restrictions: Optional[int] = Field(
        description="Operating investment income with donor restrictions. "
                    "Must be explicitly labeled. Do not assume based on other investment lines."
    )

    auxiliary_enterprise_revenue: Optional[int] = Field(
        description="Revenue from auxiliary operations (e.g., housing, dining, parking) in 2024–2025. "
                    "Must be clearly labeled."
    )

    healthcare_clinical_revenue: Optional[int] = Field(
        description="Revenue from healthcare or clinical activities for 2024–2025. "
                    "Include only if clearly identified."
    )

    net_assets_released_from_restrictions: Optional[int] = Field(
        description="Net assets released from donor or legal restrictions in 2024–2025. "
                    "Labeled 'Net Assets Released from Restrictions'."
    )

    other_operating_revenue: Optional[int] = Field(
        description="Other operating revenue not elsewhere categorized. "
                    "Only extract if labeled explicitly."
    )

    total_operating_revenue: Optional[int] = Field(
        description="Total operating revenue for 2024–2025. "
                    "Only extract if labeled. Do not compute."
    )

    # ─── FUNCTIONAL EXPENSES ─────────────────────────────────────
    instructional_expense: Optional[int] = Field(
        description="Instructional expenses for 2024–2025. "
                    "Include direct academic instruction."
    )

    research_expense: Optional[int] = Field(
        description="Research-related operational expenses for 2024–2025. "
                    "Exclude capitalized research infrastructure unless operational."
    )

    instructional_research_expense: Optional[int] = Field(
        description="Combined instruction & research expense line, if labeled together. "
                    "Only use this if reported as one item."
    )

    auxiliary_enterprise_expense: Optional[int] = Field(
        description="Expenses related to auxiliary operations (e.g., dorms, food) for 2024–2025."
    )

    healthcare_clinical_expense: Optional[int] = Field(
        description="Clinical and healthcare expense for 2024–2025. "
                    "Include only if labeled clearly."
    )

    academic_support: Optional[int] = Field(
        description="Academic support services expenses (libraries, curriculum dev) in 2024–2025."
    )

    student_services: Optional[int] = Field(
        description="Expenses related to student services (advising, career, etc.) for 2024–2025."
    )

    institutional_support: Optional[int] = Field(
        description="Institutional overhead and general administrative expenses for 2024–2025."
    )

    public_service_expense: Optional[int] = Field(
        description="Public/community service operating expenses for 2024–2025."
    )

    student_aid_expense: Optional[int] = Field(
        description="Scholarships and fellowships recognized as expense, not offsets to revenue."
    )

    other_operating_expense: Optional[int] = Field(
        description="All other functional operating expenses for 2024–2025, if labeled as 'Other Exp'."
    )

    total_operating_expense: Optional[int] = Field(
        description="Total of all functional operating expenses for 2024–2025. "
                    "Only extract if labeled."
    )

    net_operating_income: Optional[int] = Field(
        description="Net income from operations (Total Revenue - Total Expenses). "
                    "Do not compute. Only extract if labeled 'Net Operating Income' or equivalent."
    )

    # ─── NATURAL EXPENSES ────────────────────────────────────────
    plant_maintenance_expense: Optional[int] = Field(
        description="Plant operations and maintenance expense for 2024–2025."
    )

    depreciation_amortization_expense: Optional[int] = Field(
        description="Depreciation and amortization expense reported for 2024–2025."
    )

    interest_expense: Optional[int] = Field(
        description="Interest expense on borrowings reported for 2024–2025."
    )

    # ─── NON-OPERATING ACTIVITY ──────────────────────────────────
    non_op_realized_gains: Optional[int] = Field(
        description="Realized gains from investments reported as non-operating in 2024–2025."
    )

    other_non_op_revenue: Optional[int] = Field(
        description="Other non-operating revenue for 2024–2025, if not itemized elsewhere."
    )

    non_operating_revenue: Optional[int] = Field(
        description="Total non-operating revenue if explicitly labeled."
    )

    non_op_realized_losses: Optional[int] = Field(
        description="Realized losses from investments reported as non-operating in 2024–2025."
    )

    other_non_op_expense: Optional[int] = Field(
        description="Other non-operating expenses not otherwise listed."
    )

    non_operating_expense: Optional[int] = Field(
        description="Total non-operating expenses, if explicitly labeled."
    )

    non_op_realized_gains_with_restrictions: Optional[int] = Field(
        description="Realized investment gains with donor restrictions. "
                    "Only extract if explicitly labeled with restrictions."
    )

    # ─── CHANGES IN NET ASSETS ───────────────────────────────────
    extraordinary_gain_or_loss: Optional[int] = Field(
        description="Extraordinary or one-time gain/loss for 2024–2025."
    )

    net_assets_released_for_capital: Optional[int] = Field(
        description="Net assets released from restriction for capital use in 2024–2025."
    )

    change_fair_value_derivatives: Optional[int] = Field(
        description="Change in fair market value of derivative instruments."
    )

    capital_grants_gifts: Optional[int] = Field(
        description="Capital grants and gifts received during 2024–2025."
    )

    net_unrealized_investment_income: Optional[int] = Field(
        description="Net unrealized gains/losses on investments not included elsewhere."
    )

    other_adj_net_assets_without_restrictions: Optional[int] = Field(
        description="Other adjustments to net assets without donor restrictions."
    )

    change_net_assets_without_donor_restrictions: Optional[int] = Field(
        description="Net change in unrestricted net assets for 2024–2025."
    )

    change_net_assets_with_donor_restrictions: Optional[int] = Field(
        description="Net change in restricted net assets for 2024–2025."
    )

    change_temp_restricted_net_assets: Optional[int] = Field(
        description="Change in temporarily restricted net assets for 2024–2025."
    )

    change_perm_restricted_net_assets: Optional[int] = Field(
        description="Change in permanently restricted net assets for 2024–2025."
    )

    other_adj_to_net_assets: Optional[int] = Field(
        description="Other general adjustments to net assets for the period."
    )

    total_change_in_net_assets: Optional[int] = Field(
        description="Final bottom-line change in total net assets for 2024–2025. "
                    "Only extract if explicitly stated. Do not derive."
    )
