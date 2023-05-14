from web_report import WebReport


class PrintReport(WebReport):
    def format_report(self):
        report = super().format_report()
        report = report.replace('<br>', '\n')
        report = report.replace('<b>', '')
        report = report.replace('</b>', '')
        report = report.replace('</font>', '')
        report = report.replace('<font color="red">', '(')
        report = report.replace('</font>', ')')
        return report


def main():
    report = PrintReport()
    print(report.format_report())


if __name__ == '__main__':
    main()
