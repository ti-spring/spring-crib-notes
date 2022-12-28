package keel.batch.doma2.writer;

import java.util.List;

import org.springframework.batch.item.Chunk;
import org.springframework.batch.item.ItemWriter;
import org.springframework.stereotype.Component;

import keel.batch.doma2.dao.BonusDao;
import keel.batch.doma2.entity.Bonus;

// doma2-spring-batch-example-start
@Component
public class BonusWriter implements ItemWriter<Bonus> {

    private final BonusDao dao;

    public BonusWriter(BonusDao dao) {
        this.dao = dao;
    }

    @Override
    public void write(Chunk<? extends Bonus> items) {
        dao.insert((List<Bonus>) items.getItems());
    }
}
// doma2-spring-batch-example-end
