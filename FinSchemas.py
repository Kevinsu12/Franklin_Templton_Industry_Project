from typing import Optional
from pydantic import BaseModel, Field

class FinancialPosition_2024_25(BaseModel):
    year: int = Field(
        description=(
            "Fiscal year for which the data applies (e.g., 2024–2025). "
            "Only extract data for the 2024–2025 fiscal year; ignore data from other years or periods."
        )
    )
    cash_and_short_term_investments: Optional[int] = Field(
        description=(
            "Unrestricted cash, cash equivalents, and short‑term investments as of the end of the 2024–2025 fiscal year. "
            "Only extract 2024–2025 data; exclude restricted cash reported separately and any other periods. "
            "If the institution reports multiple segments or campuses, combine all."
        )
    )
    student_receivables_net: Optional[int] = Field(
        description=(
            "Net student receivables for the 2024–2025 fiscal year (after allowance for doubtful accounts). "
            "Only extract net figures; ignore gross receivables or allowances reported separately. "
            "Combine across campuses if applicable."
        )
    )
    accounts_receivable: Optional[int] = Field(
        description=(
            "Total accounts receivable as of the end of the 2024–2025 fiscal year. "
            "Only extract data for 2024–2025; exclude intercompany balances if reported separately. "
            "Combine across all reporting units."
        )
    )
    contributions_receivable: Optional[int] = Field(
        description=(
            "Pledges and contributions receivable for the 2024–2025 fiscal year. "
            "Only extract receivable amounts net of allowance; ignore contributions from other periods. "
            "Combine across campuses or programs."
        )
    )
    notes_receivable: Optional[int] = Field(
        description=(
            "Notes receivable outstanding as of the end of the 2024–2025 fiscal year. "
            "Only extract 2024–2025 amounts; combine across all segments if reported separately."
        )
    )
    loans_receivable_net: Optional[int] = Field(
        description=(
            "Net loans receivable (after allowance) for the 2024–2025 fiscal year. "
            "Only extract net figures; ignore loan loss reserves or gross balances. "
            "Combine across campuses if applicable."
        )
    )
    other_assets: Optional[int] = Field(
        description=(
            "Other assets not classified elsewhere for the 2024–2025 fiscal year. "
            "Only extract 2024–2025 data; review footnotes to avoid overlap with other categories."
        )
    )
    investments: Optional[int] = Field(
        description=(
            "Short‑ and long‑term investments as of the end of the 2024–2025 fiscal year. "
            "Only extract fair‑value amounts; exclude restricted or endowment investments if reported separately."
        )
    )
    right_of_use_assets: Optional[int] = Field(
        description=(
            "Total right‑of‑use assets recognized under ASC 842 for the 2024–2025 fiscal year. "
            "Only extract lease assets; ignore associated lease liabilities."
        )
    )
    land_buildings_equipment_net: Optional[int] = Field(
        description=(
            "Property, plant, and equipment, net of accumulated depreciation, as of the end of the 2024–2025 fiscal year. "
            "Only extract net PP&E; accumulated depreciation is reported separately. "
            "Combine across all locations if the institution has multiple campuses."
        )
    )
    accumulated_depreciation: Optional[int] = Field(
        description=(
            "Total accumulated depreciation (contra‑asset) as of the end of the 2024–2025 fiscal year. "
            "Only extract depreciation related to PP&E; confirm sign convention."
        )
    )
    rou_assets_finance_lease: Optional[int] = Field(
        description=(
            "Right‑of‑use assets under finance leases for the 2024–2025 fiscal year. "
            "Only extract finance‑lease assets; exclude operating leases."
        )
    )
    rou_assets_operating_lease: Optional[int] = Field(
        description=(
            "Right‑of‑use assets under operating leases for the 2024–2025 fiscal year. "
            "Only extract operating‑lease assets; exclude finance leases."
        )
    )
    current_portion_long_term_debt: Optional[int] = Field(
        description=(
            "Portion of long‑term debt due within one year as of the 2024–2025 fiscal year end. "
            "Only extract current maturities; ignore total long‑term debt lines."
        )
    )
    current_portion_operating_lease: Optional[int] = Field(
        description=(
            "Current portion of lease liabilities under operating leases for the 2024–2025 fiscal year. "
            "Only extract amounts due within one year; the long‑term portion is reported separately."
        )
    )
    short_term_debt: Optional[int] = Field(
        description=(
            "Short‑term borrowings (e.g., commercial paper) as of the 2024–2025 fiscal year end. "
            "Only extract amounts maturing within one year; ignore long‑term borrowings."
        )
    )
    total_assets: Optional[int] = Field(
        description=(
            "Total assets for the 2024–2025 fiscal year. "
            "Only extract if explicitly provided; otherwise sum all individual asset line items."
        )
    )
    accounts_payable: Optional[int] = Field(
        description=(
            "Trade and other payables as of the end of the 2024–2025 fiscal year. "
            "Only extract accounts payable; exclude accrued expenses."
        )
    )
    student_deposits_and_deferred_revenue: Optional[int] = Field(
        description=(
            "Student deposits and deferred revenue balances for the 2024–2025 fiscal year. "
            "Only extract deferred tuition/fees; ignore deposits from other sources."
        )
    )
    tenant_capital_improvements: Optional[int] = Field(
        description=(
            "Liabilities for tenant capital improvements as of the 2024–2025 fiscal year end. "
            "Only extract capital improvement obligations; confirm classification via footnotes."
        )
    )
    bonds_payable_net: Optional[int] = Field(
        description=(
            "Bonds payable, net of unamortized discount/premium, as of the 2024–2025 fiscal year end. "
            "Only extract net bond amounts; ignore gross issue amounts."
        )
    )
    refundable_advances_us_govt: Optional[int] = Field(
        description=(
            "Refundable government advances (e.g., Pell grants) for the 2024–2025 fiscal year. "
            "Only extract refundable advance balances; exclude nonrefundable grants."
        )
    )
    lease_obligations: Optional[int] = Field(
        description=(
            "Total lease liabilities recognized under ASC 842 for the 2024–2025 fiscal year. "
            "Only extract combined current and non‑current lease obligations."
        )
    )
    liabilities_under_split_interest_agreements: Optional[int] = Field(
        description=(
            "Liabilities under split‑interest agreements for the 2024–2025 fiscal year. "
            "Only extract these obligations; consult footnotes for detail."
        )
    )
    liabilities_associated_with_investments: Optional[int] = Field(
        description=(
            "Investment‑related liabilities (e.g., margin loans) for the 2024–2025 fiscal year. "
            "Only extract liabilities tied to investment activities; ignore other financing liabilities."
        )
    )
    non_controlling_interests: Optional[int] = Field(
        description=(
            "Non‑controlling (minority) interests in consolidated subsidiaries as of the 2024–2025 fiscal year end. "
            "Only extract equity attributable to minority shareholders."
        )
    )
    total_liabilities: Optional[int] = Field(
        description=(
            "Total liabilities for the 2024–2025 fiscal year. "
            "Only extract if provided; otherwise sum all individual liability line items."
        )
    )
    net_assets_with_donor_restrictions: Optional[int] = Field(
        description=(
            "Net assets subject to donor restrictions as of the 2024–2025 fiscal year end. "
            "Only extract donor‑restricted amounts; exclude board‑designated funds."
        )
    )
    net_assets_without_donor_restrictions: Optional[int] = Field(
        description=(
            "Net assets without donor restrictions for the 2024–2025 fiscal year. "
            "Only extract unrestricted net assets; ignore temporarily restricted categories."
        )
    )
    total_net_assets: Optional[int] = Field(
        description=(
            "Total net assets (with and without donor restrictions) for the 2024–2025 fiscal year. "
            "Only extract if provided; otherwise sum net asset lines."
        )
    )
    total_liabilities_and_net_assets: Optional[int] = Field(
        description=(
            "Total liabilities and net assets (should equal total assets) for the 2024–2025 fiscal year. "
            "Only extract provided totals; verify the balance sheet equation holds."
        )
    )
