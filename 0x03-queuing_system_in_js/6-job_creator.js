import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Create job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification!',
};

// Create a job and enqueue it
const job = queue.create('push_notification_code', jobData);

// Log job creation
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
  process.exit(0); // Exit the process after job creation
});

// Log job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Log job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
