import kue from 'kue';

// Create an array of jobs
const jobs = [
  // ... array of job objects
  // Example:
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  // ... more job objects
];

// Create a Kue queue
const queue = kue.createQueue();

// Loop through the jobs array and create jobs
jobs.forEach((jobData, index) => {
  const job = queue
    .create('push_notification_code_2', jobData)
    .save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

  // Listen for job completion
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Listen for job failure
  job.on('failed', (errorMessage) => {
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });

  // Listen for job progress
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});

// Log when jobs are being created
console.log('Creating notification jobs...');

// Process any active jobs in the queue
queue.active();

// Log when job creation is complete
console.log('Notification job creation complete.');
