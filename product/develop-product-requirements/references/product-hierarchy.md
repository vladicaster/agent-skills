# Product Hierarchy

Model only levels that carry distinct ownership or requirements:

Platform → Product → Subproduct → PRD → Requirement → Acceptance criterion.

Assign immutable IDs and mutable titles. Declare each item's parent and inherit shared requirements by reference. Put a requirement at the highest level where it is universally valid; do not copy platform security or accessibility policy into every PRD.

Before creating an ID, inspect the catalog and existing PRDs. Never reuse retired IDs. A PRD may affect multiple products or repositories, but must have one accountable owner and a declared primary location.
