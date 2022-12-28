package keel.batch.doma2;

import static org.assertj.core.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.springframework.batch.core.BatchStatus;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.JobExecution;
import org.springframework.batch.core.launch.JobLauncher;
import org.springframework.batch.core.repository.JobRepository;
import org.springframework.batch.test.JobLauncherTestUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.test.context.TestPropertySource;

@SpringBootTest
@TestPropertySource("classpath:application-test.properties")
public class Doma2SpringBatchApplicationTest {

    @Autowired
    private JobLauncherTestUtils jobLauncherTestUtils;

    @Autowired
    private JdbcTemplate template;

    @Test
    public void ジョブが正常終了すること() throws Exception {
        JobExecution jobExecution = jobLauncherTestUtils.launchJob();
        assertThat(jobExecution.getStatus())
                .isEqualTo(BatchStatus.COMPLETED);

        Integer count = template.queryForObject("select count(*) from bonus;", Integer.class);
        assertThat(count)
                .isEqualTo(11);
    }

    @TestConfiguration
    static class BatchTestConfig {

        @Bean
        JobLauncherTestUtils jobLauncherTestUtils(JobLauncher jobLauncher, Job job, JobRepository jobRepository) {
            JobLauncherTestUtils jobLauncherTestUtils = new JobLauncherTestUtils();
            jobLauncherTestUtils.setJobLauncher(jobLauncher);
            jobLauncherTestUtils.setJob(job);
            jobLauncherTestUtils.setJobRepository(jobRepository);
            return jobLauncherTestUtils;
        }
    }
}
