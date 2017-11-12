// overwrite the `languages` property to use a custom getter
Object.defineProperty(navigator, 'languages', {
    get: function () {
        return ['ko-KR', 'ko'];
    }
});

// overwrite the `plugins` property to use a custom getter
Object.defineProperty(navigator, 'plugins', {
    get: function () {
        // this just needs to have `length > 0`, but we could mock the plugins too
        return [1, 2, 3, 4, 5];
    }
});

const getParameter = WebGLRenderingContext.getParameter;
WebGLRenderingContext.prototype.getParameter = function (parameter) {
    // UNMASKED_VENDOR_WEBGL
    if (parameter === 37445) {
        return 'NVIDIA Corporation';
    }
    // UNMASKED_RENDERER_WEBGL
    if (parameter === 37446) {
        return 'NVIDIA GeForce GTX 960 OpenGL Engine';
    }
    return getParameter(parameter);
};
