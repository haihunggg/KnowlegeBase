<script>
function activateTabFromUrlFragment() {
  // 1. Get the fragment from the URL (e.g., #tab2-h1)
  const fragment = window.location.hash;

  if (fragment) {
    // 2. Find the element with the matching ID
    // We remove the '#' from the fragment to get the pure ID
    const targetElement = document.getElementById(fragment.substring(1));

    if (targetElement) {
      // 3. Find the parent .tabbed-block of the target element
      const parentBlock = targetElement.closest(".tabbed-block");

      // 4. Find the main container for all tab content blocks
      const contentContainer = targetElement.closest(".tabbed-content");

      if (parentBlock && contentContainer) {
        // 5. Get all tab blocks to determine the index of our target
        const allBlocks = Array.from(
          contentContainer.querySelectorAll(".tabbed-block"),
        );
        const targetIndex = allBlocks.indexOf(parentBlock);

        // 6. Navigate up to the main component container
        const mainContainer = contentContainer.parentElement;

        if (mainContainer) {
          // 7. Find all the labels for the tabs within that container
          const allLabels = mainContainer.querySelectorAll(
            ".tabbed-labels label",
          );

          if (allLabels[targetIndex]) {
            // 8. First, activate the correct tab by clicking its label
            allLabels[targetIndex].click();

            // 9. Now that the element is visible, scroll it into view
            targetElement.scrollIntoView({
              behavior: "smooth", // Use a smooth scrolling animation
              block: "start", // Align the top of the element with the top of the visible area
            });
          }
        }
      }
    }
  }
}

document.addEventListener('DOMContentLoaded', activateTabFromUrlFragment);
</script>