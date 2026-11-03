"""
MCP Server implementation for Ocular Macular Ganglion Cell Complex (GCC / GCIPL) Skill.
Exposes standard FastMCP-compatible tools for SD-OCT macular ganglion cell morphology and glaucoma screening.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import MacularGanglionCellComplexClient


def evaluate_macular_ganglion_cell_complex(
    average_gcc_thickness_um: float,
    superior_gcc_thickness_um: float,
    inferior_gcc_thickness_um: float,
    focal_loss_volume_flv_pct: Optional[float] = None,
    global_loss_volume_glv_pct: Optional[float] = None,
    eye_examined: Optional[str] = "OD (Right Eye)",
    patient_age_years: Optional[int] = 58
) -> str:
    """
    Evaluates macular Ganglion Cell Complex (GCC / GCIPL) thickness, asymmetry, and FLV/GLV loss volumes.
    Returns structured analysis of pre-perimetric glaucoma and optic neuropathy.
    """
    client = MacularGanglionCellComplexClient()
    result = client.evaluate_gcc(
        average_gcc_thickness_um=average_gcc_thickness_um,
        superior_gcc_thickness_um=superior_gcc_thickness_um,
        inferior_gcc_thickness_um=inferior_gcc_thickness_um,
        focal_loss_volume_flv_pct=focal_loss_volume_flv_pct,
        global_loss_volume_glv_pct=global_loss_volume_glv_pct,
        eye_examined=eye_examined,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_macular_ganglion_cell_complex",
                "description": "Calculates SD-OCT macular Ganglion Cell Complex (GCC / GCIPL) average thickness, hemifield asymmetry, and focal/global loss volumes (FLV%/GLV%) for glaucoma detection.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "average_gcc_thickness_um": {"type": "number", "description": "Average macular GCC/GCIPL thickness in micrometers (normal >= 78.0 um)"},
                        "superior_gcc_thickness_um": {"type": "number", "description": "Superior hemifield GCC thickness in um"},
                        "inferior_gcc_thickness_um": {"type": "number", "description": "Inferior hemifield GCC thickness in um"},
                        "focal_loss_volume_flv_pct": {"type": "number", "description": "Optional Focal Loss Volume in % (normal < 1.0%)"},
                        "global_loss_volume_glv_pct": {"type": "number", "description": "Optional Global Loss Volume in % (normal < 4.0%)"},
                        "eye_examined": {"type": "string", "description": "Examined eye: 'OD (Right Eye)' or 'OS (Left Eye)'"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 58)"}
                    },
                    "required": ["average_gcc_thickness_um", "superior_gcc_thickness_um", "inferior_gcc_thickness_um"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = MacularGanglionCellComplexClient()
        test_res = client.evaluate_gcc(
            average_gcc_thickness_um=84.5,
            superior_gcc_thickness_um=85.0,
            inferior_gcc_thickness_um=84.0
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
