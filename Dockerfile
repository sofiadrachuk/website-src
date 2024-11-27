# Use an official Nginx image
FROM nginx:alpine

# Copy the static HTML file to the Nginx document root
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80
