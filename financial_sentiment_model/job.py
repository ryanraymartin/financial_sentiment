from ray.job_submission import JobSubmissionClient

# If using a remote cluster, replace 127.0.0.1 with the head node's IP address.
client = JobSubmissionClient("http://35.90.72.119:8265")

job_id = client.submit_job(
    # Entrypoint shell command to execute
    entrypoint="python model_on_ray_serve.py",
    # Runtime environment for the job, specifying a working directory and pip package
    runtime_env={
        "working_dir": "./",
        "pip": ["requests==2.26.0"]
    }
)