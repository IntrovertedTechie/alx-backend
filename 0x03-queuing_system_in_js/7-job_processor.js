import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100); // Track progress at 0%

  if (blacklistedNumbers.includes(phoneNumber)) {
    job.fail(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50); // Track progress at 50%
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }

  done();
};

// Create a Kue queue with concurrency of 2 (process 2 jobs at a time)
const queue = kue.createQueue({ concurrency: 2 });

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Log when job processing starts
console.log('Processing notification jobs...');

// Log when job processing is complete
queue.on('idle', () => {
  console.log('Notification job processing complete.');
});

// Log when jobs are removed from the queue
queue.on('job remove', (id) => {
  console.log(`Job ${id} removed from queue.`);
});

// Process any active jobs in the queue
queue.active();

// Log when job processing is started
console.log('Notification job processing started.');
