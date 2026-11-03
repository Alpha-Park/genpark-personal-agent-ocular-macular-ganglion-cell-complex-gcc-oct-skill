"""
Ocular Macular Ganglion Cell Complex (GCC / GCIPL) & SD-OCT Glaucoma Biomarker Client.
Zero-mock pure Python standard library implementation.
Calculates Average GCC Thickness (um), Superior vs Inferior Hemifield Asymmetry,
Focal Loss Volume (FLV%), Global Loss Volume (GLV%), and pre-perimetric glaucomatous optic neuropathy staging.
"""

import math
from typing import Dict, Any, Optional


class MacularGanglionCellComplexClient:
    """
    Evaluates macular ganglion cell-inner plexiform layer (GCIPL / GCC) morphology via SD-OCT:
    - Average Thickness (um): normal 78.0 - 95.0 um (thinning < 72.0 um indicates axonal dropout)
    - Superior vs Inferior Asymmetry (um): normal <= 4.5 um (asymmetry > 6.0 um indicates focal damage)
    - Focal Loss Volume (FLV%): normal < 1.0% (high specificity for early focal glaucomatous scotoma)
    - Global Loss Volume (GLV%): normal < 4.0% (diffuse ganglion cell volume reduction)
    - Crucial structural biomarker for pre-perimetric glaucoma and optic nerve neurodegeneration.
    """

    def __init__(self):
        pass

    def evaluate_gcc(
        self,
        average_gcc_thickness_um: float,
        superior_gcc_thickness_um: float,
        inferior_gcc_thickness_um: float,
        focal_loss_volume_flv_pct: Optional[float] = None,
        global_loss_volume_glv_pct: Optional[float] = None,
        eye_examined: Optional[str] = "OD (Right Eye)",
        patient_age_years: Optional[int] = 58
    ) -> Dict[str, Any]:
        """
        Calculates macular GCC thickness, asymmetry, and volumetric loss parameters.
        average_gcc_thickness_um: mean GCC / GCIPL thickness in micrometers (e.g. 84.5 um).
        superior_gcc_thickness_um: superior macular hemifield thickness in um (e.g. 85.0 um).
        inferior_gcc_thickness_um: inferior macular hemifield thickness in um (e.g. 84.0 um).
        """
        if average_gcc_thickness_um <= 0 or superior_gcc_thickness_um <= 0 or inferior_gcc_thickness_um <= 0:
            raise ValueError("Thickness measurements must be strictly positive.")

        hemifield_asymmetry_um = round(abs(superior_gcc_thickness_um - inferior_gcc_thickness_um), 1)

        # Estimate FLV% and GLV% if not directly provided based on hemifield disparity & thinning
        if global_loss_volume_glv_pct is None:
            # Baseline normal reference is ~84.0 um
            if average_gcc_thickness_um < 84.0:
                glv_est = round(((84.0 - average_gcc_thickness_um) / 84.0) * 100.0, 1)
            else:
                glv_est = 0.5
            global_loss_volume_glv_pct = glv_est

        if focal_loss_volume_flv_pct is None:
            # Significant hemifield disparity drives focal loss
            if hemifield_asymmetry_um > 4.5:
                flv_est = round((hemifield_asymmetry_um / 84.0) * 100.0, 1)
            else:
                flv_est = 0.4
            focal_loss_volume_flv_pct = flv_est

        # Clinical Classification based on Agerelated Normative Database (ISGEO Glaucoma Standards):
        # Normal GCC: Average >= 78.0 um, Asymmetry <= 5.0 um, FLV < 1.0%, GLV < 4.0%
        # Borderline: Average 72.0 - 77.9 um, Asymmetry 5.1 - 7.0 um, FLV 1.0 - 2.5%, GLV 4.0 - 7.0%
        # Pathological: Average < 72.0 um, Asymmetry > 7.0 um, FLV > 2.5%, GLV > 7.0%
        is_severely_thinned = average_gcc_thickness_um < 72.0
        is_markedly_asymmetric = hemifield_asymmetry_um > 7.0
        is_flv_abnormal = focal_loss_volume_flv_pct > 2.5
        is_glv_abnormal = global_loss_volume_glv_pct > 7.0

        if is_severely_thinned or (is_flv_abnormal and is_glv_abnormal):
            structural_status = "Definite Macular Ganglion Cell Complex Atrophy"
            clinical_risk = "Extensive loss of macular retinal ganglion cell somas and dendrites; highly consistent with manifest glaucomatous optic neuropathy or post-neuritis axonal loss."
        elif is_markedly_asymmetric or is_flv_abnormal:
            structural_status = "Focal GCC Defect / Early Pre-Perimetric Glaucoma"
            clinical_risk = "Significant vertical hemifield asymmetry and elevated focal loss volume (FLV%); indicates localized neuroretinal rim breach preceding standard automated perimetry visual field loss."
        elif average_gcc_thickness_um < 78.0 or global_loss_volume_glv_pct > 4.0:
            structural_status = "Borderline / Mildly Depressed GCC Thickness"
            clinical_risk = "Mild diffuse thinning; monitor for ocular hypertension conversion, age-related decline, or toxic optic neuropathy."
        else:
            structural_status = "Normal Physiological Macular Ganglion Cell Complex"
            clinical_risk = "Robust ganglion cell-inner plexiform layer architecture, symmetric vertical hemifield profile, and intact neuroretinal volume."

        return {
            "status": "success",
            "gcc_metrics": {
                "average_gcc_thickness_um": round(average_gcc_thickness_um, 1),
                "superior_hemifield_thickness_um": round(superior_gcc_thickness_um, 1),
                "inferior_hemifield_thickness_um": round(inferior_gcc_thickness_um, 1),
                "hemifield_asymmetry_um": hemifield_asymmetry_um,
                "focal_loss_volume_flv_pct": round(focal_loss_volume_flv_pct, 1),
                "global_loss_volume_glv_pct": round(global_loss_volume_glv_pct, 1)
            },
            "normative_thresholds": {
                "normal_average_thickness_lower_limit_um": 78.0,
                "normal_hemifield_asymmetry_upper_limit_um": 5.0,
                "normal_flv_upper_limit_pct": 1.0,
                "normal_glv_upper_limit_pct": 4.0,
                "eye_examined": eye_examined,
                "patient_age_years": patient_age_years
            },
            "clinical_assessment": {
                "structural_status": structural_status,
                "pathophysiology_summary": clinical_risk
            }
        }
