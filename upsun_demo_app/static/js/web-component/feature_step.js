class FeatureStep extends HTMLElement {
    constructor() {
        super();
        // No Shadow DOM to allow Tailwind CSS to apply globally
    }

    connectedCallback() {
        this.initializeState();
        this.extractContent();
        this.render();
        this.setupEventListeners();
    }

    /**
     * Initialize the state based on attributes.
     */
    initializeState() {
        this.title = this.getAttribute('title') || 'Default Title';
        this.isDisabled = this.hasAttribute('disabled');
        this.isCurrentStep = this.hasAttribute('current-step');
        this.isCompleted = this.hasAttribute('completed');
        this.canRevealContent = this.isCurrentStep || this.isCompleted;
    }

    /**
     * Extract content from child elements.
     */
    extractContent() {
        this.image = this.querySelector('feature-image')?.innerHTML || '';
        this.content = this.querySelector('feature-content')?.innerHTML || 'Default content';
    }

    /**
     * Generate the inner HTML structure based on the state.
     */
    render() {
        this.innerHTML = `
            <div class="feature--step flex flex-col transition-all duration-300 ${this.isDisabled ? 'is-disabled' : ''} group-hover:opacity-100 relative">
                <div class="aside-title flex flex-row gap-4 items-center">
                    ${this.image}
                    <h2 class="font-semibold">${this.title}</h2>
                </div>
                <div class="border-l-2 ml-5 pl-10">
                    <div class="rounded-lg p-4 bg-upsun-black-900 ${!this.canRevealContent ? 'hidden' : ''}">
                        <div class="feature--content ${this.isDisabled ? 'line-clamp-1' : ''}">${this.content}</div>
                    </div>
                </div>
            </div>
        `;

        if (!this.canRevealContent) {
            this.addCompletionMessage();
        }

        if (this.shouldShowToggleButton()) {
            this.addToggleButton();
        }
    }

    /**
     * Determine if the toggle button should be displayed.
     * @returns {boolean}
     */
    shouldShowToggleButton() {
        return this.canRevealContent && !this.isCurrentStep && this.isCompleted;
    }

    /**
     * Add a message prompting the user to complete the current step.
     */
    addCompletionMessage() {
        const message = document.createElement('span');
        message.className = "opacity-0 group-hover:opacity-100 transition-opacity duration-200 text-white pt-1 pr-1 cursor-default absolute top-0 right-0";
        message.textContent = "Complete current step to proceed.";
        this.appendChild(message);
    }

    /**
     * Add the "Show more"/"Show less" toggle button.
     */
    addToggleButton() {
        const button = document.createElement('button');
        button.className = "toggle-more opacity-0 group-hover:opacity-100 transition-opacity duration-200 text-white pt-1 pr-1 cursor-pointer absolute top-0 right-0 hover:underline";
        button.style.pointerEvents = "auto";
        button.textContent = this.isDisabled ? 'Show more' : 'Show less';
        this.appendChild(button);
    }

    /**
     * Setup event listeners for interactive elements.
     */
    setupEventListeners() {
        const button = this.querySelector('button.toggle-more');
        if (button) {
            const featureStep = this.querySelector('.feature--step');
            const featureContent = this.querySelector('.feature--content');

            button.addEventListener('click', () => {
                this.toggleContent(featureStep, featureContent, button);
            });
        }
    }

    /**
     * Toggle the visibility of the content and update the button text.
     * @param {HTMLElement} featureStep
     * @param {HTMLElement} featureContent
     * @param {HTMLButtonElement} button
     */
    toggleContent(featureStep, featureContent, button) {
        featureStep.classList.toggle('is-disabled');
        featureContent.classList.toggle('line-clamp-1');

        const isNowDisabled = featureStep.classList.contains('is-disabled');
        button.textContent = isNowDisabled ? 'Show more' : 'Show less';
    }
}

function copyToClipboard(button) {
    const textElement = button.querySelector('.copy-text');
    const text = textElement.innerText;

    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            showCopiedMessage(button);
        }).catch(err => {
            console.error('Could not copy text: ', err);
            alert('Failed to copy text, please try manually.');
        });
    } else {
        // Fallback for browsers that do not support Clipboard API
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        try {
            document.execCommand('copy');
            showCopiedMessage(button);
        } catch (err) {
            console.error('Fallback: Oops, unable to copy', err);
            alert('Failed to copy text, please try manually.');
        }
        document.body.removeChild(textarea);
    }
}

function showCopiedMessage(button) {
    const copyMessage = button.querySelector('.copied-indicator');
    copyMessage.classList.remove('opacity-0');
    copyMessage.classList.add('opacity-100');

    setTimeout(() => {
        copyMessage.classList.remove('opacity-100');
        copyMessage.classList.add('opacity-0');
    }, 2500);
}

// Register the custom element
    customElements.define('feature-step', FeatureStep);
