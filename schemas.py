from typing import Optional
from pydantic import BaseModel, Field

class Enrollment2024_25(BaseModel):
    Undergraduate_Headcount: Optional[int] = Field(
        description=(
            "Total undergraduate headcount for the 2024–2025 academic year "
            "(Different than undergraduate FTE. Sometimes you need to combine both full-time and part time)."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
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
    Professional_Headcount: Optional[int] = Field(
        description=(
            "Combined professional school headcount (e.g. med, law) for 2024–2025 "
            "(Different than professional FTE. Sometimes you need to combine both full-time and part time)."
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

    Undergraduate_FTE: Optional[int] = Field(
        description=(
            "Undergraduate full-time headcount or FTE for 2024–2025 "
            "(may appear as “FT”, “Full-Time”, or “FTE”)."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    Graduate_FTE: Optional[int] = Field(
        description=(
            "Graduate full-time headcount or FTE for 2024–2025 "
            "(may appear as “FT”, “Full-Time”, or “FTE”)."
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
            "(may appear as “FT”, “Full-Time”, or “FTE”)."
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

    Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total applications received for the 2024–2025 cycle. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    
    Acceptances: Optional[int] = Field(
        description=(
            "Total acceptances for the 2024–2025 cycle. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
        )
    )
    Matriculants: Optional[int] = Field(
        description=(
            "Number of students who matriculated in Fall 2024 / 2024–2025. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
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