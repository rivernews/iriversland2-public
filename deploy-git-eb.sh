source deploy-git-prep.sh && \
eb deploy && echo "SUCCESS: Deployed on elastic beanstalk. Please allow 30 sec to 1 min for the server to apply the new code base." && \
cd .. && return

echo "ERROR: See message above."