from typing import Optional
from pydantic import BaseModel, Field

class Enrollment2024_25(BaseModel):
    Undergraduate_Headcount: Optional[int] = Field(
        description=(
            "Total undergraduate headcount for the 2024–2025 academic year "
            "(Different than undergraduate FTE. Sometimes you need to combine both full-time and part time)."
            "Don't assume the table is the undergraduate Headcount unless it's specified in the table."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    
    Undergraduate_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Undergraduate full-time or FT headcount for the 2024–2025 academic year. "
            "This is different than FTE(full-time equivalent)."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc. "
            "Ignore any data from other years or terms. "
            "Combine across all campuses if the institution has multiple locations."
        )
    )
    Undergraduate_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Undergraduate part-time (PT) headcount for the 2024–2025 academic year. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc. "
            "Ignore any data from other years or terms. "
            "Combine across all campuses if the institution has multiple locations."
        )
    )
    Graduate_Headcount: Optional[int] = Field(
        description=(
            "Total graduate headcount for the 2024–2025 academic year "
            "(Different than graduate FTE. Sometimes you need to combine both full-time and part time), "
            "Combine enrollment across all graduate schools (e.g. Business, Education, etc.), "
            "which may be labeled “GR”, “Grad”, or “Graduate”. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicabl.e"
        )
    )
    Graduate_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Graduate full-time (FT) headcount for the 2024–2025 academic year. "
            "This is different than FTE(full-time equivalent)."
            "Combine across all graduate schools. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc. "
            "Ignore any data from other years or terms. "
            "Combine across campuses if needed."
        )
    )
    Graduate_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Graduate part-time (PT) headcount for the 2024–2025 academic year. "
            "Combine across all graduate schools. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc. "
            "Ignore any data from other years or terms. "
            "Combine across campuses if needed."
        )
    )
    Professional_Headcount: Optional[int] = Field(
        description=(
            "Combined professional school headcount (e.g. med, law) for 2024–2025 "
            "(Different than professional FTE. Sometimes you need to combine both full-time and part time)."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )

    Non_Degree_Headcount: Optional[int] = Field(
        description=(
            "(Different than Non-Degree FTE. Sometimes you need to combine both full-time and part time)."
            "Sometimes, Non-Degree is listed as Non-credit"
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    Total_Headcount: Optional[int] = Field(
        description=(
            "Overall student headcount for 2024–2025 "
            "(if not given, sum undergrad + grad + professional headcounts)."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )

    Total_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Total full-time headcount for 2024–2025 across all student categories. "
            "This is different than FTE(full-time equivalent)."
            "If not explicitly provided, sum Undergraduate_Headcount_Full_Time + Graduate_Headcount_Full_Time. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024. "
            "Ignore any data from other years or terms."
        )
    )
    Total_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Total part-time headcount for 2024–2025 across all student categories. "
            "If not explicitly provided, sum Undergraduate_Headcount_Part_Time + Graduate_Headcount_Part_Time. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024. "
            "Ignore any data from other years or terms."
        )
    )

    Undergraduate_FTE: Optional[int] = Field(
        description=(
            "Undergraduate full-time equivalent headcount or FTE for 2024–2025 "
            "FTE (full-time equivalent) is different than full-time, or FT."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    Graduate_FTE: Optional[int] = Field(
        description=(
            "Graduate full-time headcount or FTE for 2024–2025 "
            "FTE (full-time equivalent) is different than full-time, or FT."
            "Combine enrollment across all graduate schools (e.g. Business, Education, etc.), "
            "which may be labeled “GR”, “Grad”, or “Graduate”. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    Professional_FTE: Optional[int] = Field(
        description=(
            "Professional school full-time headcount or FTE for 2024–2025 "
            "FTE (full-time equivalent) is different than full-time, or FT."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    Total_Full_Time_Equivalent_Students: Optional[int] = Field(
        description=(
            "Total full-time equivalent students (FTE) for the 2024–2025 academic year."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )

    Undergraduate_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total undergraduate applications received for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )
    Graduate_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total graduate applications received for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )
    Transfer_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total transfer applications received for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )

    # acceptances by type
    Undergraduate_Acceptances: Optional[int] = Field(
        description=(
            "Total undergraduate acceptances for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )
    Graduate_Acceptances: Optional[int] = Field(
        description=(
            "Total graduate acceptances for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )
    Transfer_Acceptances: Optional[int] = Field(
        description=(
            "Total transfer acceptances for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )

    # matriculants by type
    Undergraduate_Matriculants: Optional[int] = Field(
        description=(
            "Number of undergraduate students who matriculated in Fall 2024 / 2024–2025. "
            "Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )
    Graduate_Matriculants: Optional[int] = Field(
        description=(
            "Number of graduate students who matriculated in Fall 2024 / 2024–2025. "
            "Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )
    Transfer_Matriculants: Optional[int] = Field(
        description=(
            "Number of transfer students who matriculated in Fall 2024 / 2024–2025. "
            "Ignore other years/terms. "
            "Combine all campuses if applicable."
        )
    )
    Retention_Rate: Optional[float] = Field(
        description=(
            "Retention rate % for the 2024–2025 entering class. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )

    Full_Time_Employee_Equivalents: Optional[int] = Field(
        description=(
            "Full-time employee equivalents (staff/faculty) in 2024–2025. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    Tuition: Optional[int] = Field(
        description=(
            "Undergraduate tuition rate for the 2024–2025 academic year. "
            "This is different than revenue generated by tuition or any financial accounting data"
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so average the tuition per student per campus"
        )
    )
    Room_and_Board_20_meals: Optional[int] = Field(
        description=(
            "Room & board cost (20-meal plan) for the 2024–2025 year. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )