
# Strategy Pattern
class ReportGenerator:

    # DI - Dependency Inversion
    def __init__(self, report_strategy):
        self.strategy = report_strategy

    def create_content(self, rides):
        builder = [self.strategy._create_headers("Taxi Report"), self.strategy._create_table_headers()]
        for ride in rides:
            builder.append(self.strategy._add_ride(ride))
        builder.append(self.strategy._close_table_headers())
        return "".join(builder)

    def create_file(self, content: str):
        self.strategy.create_file(content)
