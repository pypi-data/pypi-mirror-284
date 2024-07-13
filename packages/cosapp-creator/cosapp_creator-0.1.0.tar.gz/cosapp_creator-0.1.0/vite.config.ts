import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: './cosapp_creator/dist',
    emptyOutDir: true,
    chunkSizeWarningLimit: 1000,
    rollupOptions: {
      output: {
        manualChunks: id => {
          if (id.includes('highlight.js'))
            return id
              .toString()
              .split('node_modules/')[1]
              .split('/')[0]
              .toString();
        }
      }
    }
  }
});
