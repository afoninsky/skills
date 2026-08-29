# Responsive and adaptive contract

Status: Draft

Describe observable layout transitions, minimum/maximum composition rules, intermediate-width behavior, orientation, safe areas, software keyboard, input modes, zoom/reflow, text scaling, and intentional platform adaptation. Avoid device-name breakpoints without a layout reason.

## Representative platform matrix

| Platform class | Target/configuration | Source/runtime ownership | States/adaptations exercised | Evidence or explicit exclusion |
| --- | --- | --- | --- | --- |

Include at least one row for every materially distinct implementation/adaptation class in scope. For a shared web wrapper, keep the common browser UI and packaged-shell behavior as separate rows without inventing a native component duplicate.
