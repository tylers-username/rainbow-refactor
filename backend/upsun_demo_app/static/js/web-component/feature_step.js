class FeatureStep extends HTMLElement {
    constructor() {
        super();
        // No Shadow DOM to allow Tailwind CSS to apply globally
    }

    connectedCallback() {
        // Extract attributes or use default slots
        const title = this.getAttribute('title') || 'Default Title';
        const image = this.querySelector('feature-image')?.innerHTML || '';
        const content = this.querySelector('feature-content')?.innerHTML || 'Default content';
        const isDisabled = this.hasAttribute('disabled');
        const isCurrentStep = this.hasAttribute('current-step');
        const isCompleted = this.hasAttribute('completed');
        const canRevealContent = isCurrentStep || isCompleted;

        console.log("feature step is disabled:", isDisabled)

        // Set the inner HTML structure
        this.innerHTML = `
            <div class="feature--step flex flex-col transition-all duration-300 ${isDisabled ? 'is-disabled' : ''} group-hover:opacity-100">
              <div class="aside-title flex flex-row gap-4 items-center">
                ${image}
                <h2 class="font-semibold">${title}</h2>
              </div>
              <div class="border-l-2 ml-5 pl-10">
                <div class="rounded-lg p-4 bg-upsun-black-900 ${!canRevealContent ? 'hidden' : ''}">
                    <div class="feature--content ${isDisabled ? 'line-clamp-1' : ''}">${content}</div>
                </div>
              </div>
            </div>
        `;

        if (!canRevealContent) {
            this.innerHTML += `<span class="opacity-0 group-hover:opacity-100 transition-opacity duration-200 text-white pt-1 pr-1 cursor-default absolute top-0 right-0">
              Complete current step to proceed.
            </span>`
        }

        if (!isCurrentStep && canRevealContent) {
            this.innerHTML += `<button
              class="toggle-more opacity-0 group-hover:opacity-100 transition-opacity duration-200 text-white pt-1 pr-1 cursor-pointer absolute top-0 right-0 hover:underline"
              style="pointer-events: auto;">
              Show more
            </button>`
            // Reference elements
            const button = this.querySelector('button.toggle-more');
            const featureStep = this.querySelector('.feature--step');
            const featureContent = this.querySelector('.feature--content');

            // Toggle functionality
            button.addEventListener('click', () => {
                featureStep.classList.toggle('is-disabled');
                featureContent.classList.toggle('line-clamp-1');
                button.textContent = featureStep.classList.contains('is-disabled') ? 'Show more' : 'Show less';
            });
        }
    }
}

// Register the custom element
customElements.define('feature-step', FeatureStep);
