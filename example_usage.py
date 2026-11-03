"""
Example usage for Ocular Macular Ganglion Cell Complex (GCC / GCIPL) Skill.
"""

from client import MacularGanglionCellComplexClient


def main():
    client = MacularGanglionCellComplexClient()

    print("--- Case 1: Healthy Symmetrical Macular Ganglion Cell Complex ---")
    healthy_case = client.evaluate_gcc(
        average_gcc_thickness_um=85.2,
        superior_gcc_thickness_um=85.8,
        inferior_gcc_thickness_um=84.6,
        focal_loss_volume_flv_pct=0.4,
        global_loss_volume_glv_pct=1.2,
        eye_examined="OD (Right Eye)",
        patient_age_years=42
    )
    print("Average GCC Thickness:", healthy_case["gcc_metrics"]["average_gcc_thickness_um"], "um")
    print("Hemifield Asymmetry:", healthy_case["gcc_metrics"]["hemifield_asymmetry_um"], "um")
    print("FLV%:", healthy_case["gcc_metrics"]["focal_loss_volume_flv_pct"], "%")
    print("GLV%:", healthy_case["gcc_metrics"]["global_loss_volume_glv_pct"], "%")
    print("Structural Status:", healthy_case["clinical_assessment"]["structural_status"])
    print("Pathophysiology:", healthy_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Early Pre-Perimetric Glaucoma (Focal Inferior Loss) ---")
    glaucoma_case = client.evaluate_gcc(
        average_gcc_thickness_um=77.5,
        superior_gcc_thickness_um=82.0,
        inferior_gcc_thickness_um=73.0,
        focal_loss_volume_flv_pct=3.2,
        global_loss_volume_glv_pct=4.8,
        eye_examined="OS (Left Eye)",
        patient_age_years=61
    )
    print("Hemifield Asymmetry:", glaucoma_case["gcc_metrics"]["hemifield_asymmetry_um"], "um")
    print("FLV%:", glaucoma_case["gcc_metrics"]["focal_loss_volume_flv_pct"], "%")
    print("Structural Status:", glaucoma_case["clinical_assessment"]["structural_status"])
    print("Pathophysiology:", glaucoma_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Advanced Glaucomatous Ganglion Cell Drop-out ---")
    advanced_case = client.evaluate_gcc(
        average_gcc_thickness_um=64.0,
        superior_gcc_thickness_um=66.0,
        inferior_gcc_thickness_um=62.0,
        focal_loss_volume_flv_pct=5.8,
        global_loss_volume_glv_pct=14.5,
        eye_examined="OD (Right Eye)",
        patient_age_years=74
    )
    print("Average GCC Thickness:", advanced_case["gcc_metrics"]["average_gcc_thickness_um"], "um")
    print("GLV%:", advanced_case["gcc_metrics"]["global_loss_volume_glv_pct"], "%")
    print("Structural Status:", advanced_case["clinical_assessment"]["structural_status"])


if __name__ == "__main__":
    main()
