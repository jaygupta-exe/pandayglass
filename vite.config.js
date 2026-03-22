import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        gallery: resolve(__dirname, 'gallery.html'),
        services: resolve(__dirname, 'services.html'),
        contact: resolve(__dirname, 'contact.html'),
        about: resolve(__dirname, 'about.html'),
        hardware: resolve(__dirname, 'hardware.html'),
        'mirror-work': resolve(__dirname, 'mirror-work.html'),
        'glass-work': resolve(__dirname, 'glass-work.html'),
        railing: resolve(__dirname, 'railing.html'),
      },
    },
  },
});
