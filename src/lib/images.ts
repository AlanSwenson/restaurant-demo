import fs from 'node:fs/promises';
import path from 'node:path';

export async function getCarouselImages(): Promise<string[]> {
  try {
    const imagesDir = path.join(process.cwd(), 'public/img/restaurant/carousel');
    const files = await fs.readdir(imagesDir);
    return files.filter(file => 
      /\.(jpg|jpeg|png|gif|webp)$/i.test(file)
    );
  } catch (error) {
    console.error('Error loading carousel images:', error);
    // Return some default image names if real ones aren't available yet
    return [
      'restaurant1.jpg',
      'restaurant2.jpg',
      'restaurant3.jpg'
    ];
  }
} 